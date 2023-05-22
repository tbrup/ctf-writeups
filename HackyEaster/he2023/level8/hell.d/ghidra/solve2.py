import sys
from tree_sitter import Language, Parser, Tree

C_LANGUAGE = Language('./my-languages.so', 'c')

def read_callable(byte_offset, point):
    return src[byte_offset:byte_offset+1]

def bytes2lines(b : bytes):
    s = b.decode('utf8')
    return s.replace('\r', '').split('\n')

def lines2bytes(lst):
    return ''.join(lst).encode('utf8')

def drop_from_to(lines, start, end):
    if start[0] == end[0]:
        tmp = f'{lines[start[0]][:start[1]]}{lines[start[0]][end[1]:]}'
        lines[start[0]] = tmp
    else:
        lines[start[0]] = lines[start[0]][:start[1]]
        for line in range(start[0]+1, end[0]):
            lines[line] = '' 
        lines[end[0]] = lines[start[0]][:end[1]]
    return lines

def walk(tree: Tree):
    cursor = tree.walk()

    reached_root = False
    while not reached_root:
        yield cursor.node

        if cursor.goto_first_child():
            continue
        if cursor.goto_next_sibling():
            continue
        retracing = True
        while retracing:
            if not cursor.goto_parent():
                retracing = False
                reached_root = True

            if cursor.goto_next_sibling():
                retracing = False


def replace_while_binary(src, lines):    
    parser = Parser()
    parser.set_language(C_LANGUAGE)
    tree = parser.parse(src)
    for node in walk(tree):
        if node.type == 'while_statement':
            # print(node)
            start, end = node.start_point, node.end_point
            # print(lines[start[0]])
            # print(lines[end[0]])
            cond = node.child_by_field_name('condition')
            if cond.type == 'parenthesized_expression':
                expr = cond.children[1]
                if expr.type == 'binary_expression':
                    # print('XXXXXXXXXXXXXXXXXX')
                    l = lines[start[0]][start[1]:cond.end_point[1]]
                    # print(l)
                    l1 = f'{" "*start[1]}if {lines[cond.start_point[0]][cond.start_point[1]:]}'
                    # print(l1)
                    lines[start[0]] = l1
    return lines    
                    

def replace_do_while(src, lines):    
    parser = Parser()
    parser.set_language(C_LANGUAGE)
    tree = parser.parse(src)  # read_callable)
    for node in walk(tree):
        if node.type == 'do_statement':
            # only replace while (eax < 0x1234556), leave other untouched
            pe = node.children[3]
            be = pe.children[1]
            fun = be.children[1]
            if fun.type == '<':
                start, end = node.start_point, node.end_point
                comp = node.children[1]
                for st in comp.children:
                    if st.type == '{':
                        opening = st
                    elif st.type == '}':
                        closing = st
                if start[0] == comp.start_point[0]: # all on one line
                    lines[start[0]] = ''
                else:
                    lines = drop_from_to(lines, start, opening.end_point)
                lines = drop_from_to(lines, closing.start_point, end)
    return lines


def replace_else(src, lines):    
    parser = Parser()
    parser.set_language(C_LANGUAGE)
    tree = parser.parse(src)
    for node in walk(tree):
        if node.type == 'if_statement':
            if alt := node.child_by_field_name('alternative'):
                else_s = node.children[3]
                start, end = else_s.start_point, alt.end_point
                lines[start[0]] = f'{lines[start[0]][:start[1]]}{lines[start[0]][else_s.end_point[1]:]}'
    return lines


# remove guards of the form if (var < 0x12344) { ... }
def replace_if_lt(src, lines):    
    parser = Parser()
    parser.set_language(C_LANGUAGE)
    tree = parser.parse(src)
    for node in walk(tree):
        if node.type == 'if_statement':
            start, end = node.start_point, node.end_point
            pe = node.children[1]
            be = pe.children[1]
            left = be.child_by_field_name('left')
            right = be.child_by_field_name('right')
            op = be.children[1]
            if op.type == '<' and \
                ((left.type == 'identifier') and (right.type == 'number_literal') \
                 or (left.type == 'number_literal') and (right.type == 'identifier')):
                # if (eax < 0x123 ) { ... }
                # drop everything unless it contains a local variable
                print(start, end)
                print('XXXXXXXXXXXXXXXXXX')
                print(lines[start[0]])
                if 'local' not in lines[start[0]]:
                    lines[start[0]] = lines[start[0]][:start[1]]
                    # print(lines[start[0]])
                    # print(lines[end[0]])
                    comp = node.children[2]
                    for closing in comp.children:
                        if closing.type == '}':
                            print(closing)
                            print(lines[end[0]])
                            lines[end[0]] = lines[end[0]][:closing.start_point[1]-2]
                            print(lines[end[0]])

    return lines


def invert_pe(node):
    pe = node.children[1]
    be = pe.children[1]
    left = be.child_by_field_name('left').text.decode('utf-8')
    right = be.child_by_field_name('right').text.decode('utf-8')
    op = be.children[1]
    if op.type == '!=':
        new_op = '=='
    elif op.type == '==':
        new_op = '!='
    return f'({left} {new_op} {right})' 

def replace_while_break(src, lines):    
    parser = Parser()
    parser.set_language(C_LANGUAGE)
    tree = parser.parse(src)
    for node in walk(tree):
        if node.type == 'while_statement':
            start, end = node.start_point, node.end_point
            cond = node.child_by_field_name('condition')
            pe = cond.children[1] 
            if pe.type == 'true':
                body = node.child_by_field_name('body')
                for s in body.children:
                    if s.type == 'if_statement' and \
                        s.child_by_field_name('consequence').type == 'break_statement':
                        # we have found the break statement for the while statement
                        pe = s.children[1]
                        be = pe.children[1]
                        op = be.children[1]
                        inv_pe = invert_pe(s)
                        if op.type == '!=':
                            # in this case, we drop the while(true) statement and invert the if statement
                            # print('XXXXXXXXXXXXXXXXXX')
                            for st in body.children:
                                if st.type == '{':
                                    opening = st
                            lines = drop_from_to(lines, node.start_point, opening.end_point) 
                            lines = drop_from_to(lines, s.start_point, s.end_point)
                            lines[s.start_point[0]] = f'{lines[s.start_point[0]][:s.start_point[1]]}if {inv_pe} ' + ' {'
                        elif op.type == '==':
                            # in this case, the break is the loop exit statement
                            # --> use while (inverted condition) as loop criterion
                            res = f'{lines[start[0]][:node.children[0].end_point[1]]}'
                            res += f' {inv_pe} '
                            res += f'{lines[start[0]][node.children[2].start_point[1]:]}'
                            # print(res)
                            lines[start[0]] = res
                                                                           
                            # delete the if statement                                                    
                            lines = drop_from_to(lines, s.start_point, s.end_point)
                            # # print(lines[op.start_point[0]])
                            # lines[op.start_point[0]] = ''
                            # print(lines[op.start_point[0]])
                        break
    return lines


if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) < 2:
        print(f'usage: {sys.argv[0]} prog.c')
    else:
        with open(sys.argv[1], 'rb') as inF:
            src = inF.read()
            lines = bytes2lines(src)

        lines = replace_while_binary(src, lines)
        
        neu = ''.join(f'{l}\n' for l in lines)
        lines = replace_else(neu.encode('utf8'), lines)

        neu = ''.join(f'{l}\n' for l in lines)
        lines = replace_do_while(neu.encode('utf8'), lines)

        neu = ''.join(f'{l}\n' for l in lines)
        lines = replace_while_break(neu.encode('utf8'), lines)

        neu = ''.join(f'{l}\n' for l in lines)
        lines = replace_if_lt(neu.encode('utf8'), lines)

        neu = ''.join(f'{l}\n' for l in lines)
        with open('new.c', 'w') as outF:
            outF.write(neu)