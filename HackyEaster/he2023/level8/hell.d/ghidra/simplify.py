import re

do_while_re = re.compile(r'(do)\s+\{\s+([\s\S]*)\n\s+\}\s+while\s+\([^)]+<[^)]+\)(;)', re.M) 
while_break_re = re.compile(r'(do)\s+\{\s+([\s\S]*)\n\s+\}\s+while\s+\([^)]+<[^)]+\)(;)', re.M) 

def do_while_find_matching_while(src, start):
    next_re = re.compile(r'(do \{|\} while)')
    lt_re = re.compile(r'(\} while \([abcdefx\d]+ < \w+\);)')
    nOpen = 0
    tmp = src[start:]
    # print(f'src: {tmp[:40]} {start}')

    for match in next_re.finditer(src[start:]):
        if match[1] == 'do {':
            nOpen += 1
        else:
            nOpen -= 1
        # print(match[1], nOpen, match.start(1))
        if nOpen == 0:
            return _extracted_from_do_while_find_matching_while_(src, match, start, lt_re)
    return -1,-1


# TODO Rename this here and in `do_while_find_matching_while`
def _extracted_from_do_while_find_matching_while_(src, match, start, lt_re):
    tmp = src[match.start(1)+start:]
    # print(f'src: {tmp[:40]}\nXXXXX {match.start(1)}')
    match2 = lt_re.search(tmp[:40])
    if match2 is None:
        # print(tmp[:40])
        return -1,-1
    while_start = match.start(1) + start
    while_end = while_start + match2.end(1)
    # print(src[while_start:while_end], '\nXXXXX', match2.start(1), match2.end(1))
    return while_start, while_end

def replace_do_while(src):
    do_re = re.compile(r'(do \{\s)', re.MULTILINE)
    # while_re = re.compile( r'(\}\s+while\s+\([xabcdef\d]+ < [^)]+\);\s)', re.MULTILINE);

    match = do_re.search(src, re.MULTILINE)
    res = ''
    while match is not None:
        # print(match[1],match.start(1))
        while_index, while_index_end = do_while_find_matching_while(src, match.start(1))
        if while_index > 0:
            # print(match[1], match.start(1), while_index, while_index_end, f'{src[while_index:while_index_end]}')
            res += f'{src[:match.start(1)]} '
            src = f'{src[match.end(1)+1:while_index]} {src[while_index_end:]}'
        else:
            res += f'{src[:match.end(1)]} '
            src = f'{src[match.end(1)+1:]}'
        match = do_re.search(src, re.MULTILINE)
        

    return res




def replace_inner_while(src):
    inner_while_re = re.compile(r'(.*)while\s+(\([^)]+\))\s+(\{[^}]+\})(.*)', re.MULTILINE)
    match = inner_while_re.search(src)
    while match is not None:
        # print(match[2])
        # print(match[3])
        src = f'{src[:match.end(1)]}if {match[2]} {match[3]} {src[match.start(4):]}'
        match = inner_while_re.search(src)
    return src


#  if (eax != 0x7d59fadb) break;        if (eax == 0x7d59fadb) {
#     eax = 0x3e128c3b;                     eax = 0x3e128c3b;
#  }                                    }
def replace_while_break(src):
    if_break_re = re.compile(r'if\s+\((\w+) != ([xabcdef\d]+)\) break;([^}]+\})', re.MULTILINE)
    while_re = re.compile( r'(while\( true \) \{\s)', re.MULTILINE);
    match = if_break_re.search(src)
    while match is not None:
        # print(match[1])
        # print(match[2])
        # print(match[3])
        match2 = while_re.search(src)
        old_end = -1
        if match2 is not None:
            for match2 in while_re.finditer(src):
                # print(match2[1])
                if match2.end(1) >= match.start(1):
                    break
                old_start = match2.start(1)
                old_end = match2.end(1)
            match2 = if_break_re.search(src)

        br = '{'
        # print(src[:old_start])
        # print(src[old_end:match.start(1)])
        # print(f'{match[1]} == {match[2]}) {br} {match[3]}')
        src = f'{src[:old_start]} {src[old_end:match.start(1)]} {match[1]} == {match[2]}) {br} {match[3]} {src[match.end(3):]}'
        # print(src)
        match = if_break_re.search(src)

    return src

    
def drop_else(src):
    else_re = re.compile(r'else ')
    (src, nsub) = else_re.subn('', src)
    return src

def find_matching(src, start, opening, closing):
    br_re = re.compile(f'([{opening}{closing}])')
    nOpen = 1
    for match in br_re.finditer(src[start:]):
        # print(match[1], nOpen, match.start(1))
        if match[1] == opening:
            nOpen += 1
        else:
            nOpen -= 1
            
        if nOpen == 0:
            return match.start(1)
    return -1
    
    
def drop_if_less_than(src):
    if_re = re.compile(r'(if\s+)\(\w+ < [xabcdef\d]+\) (\{)', re.MULTILINE)
    match = if_re.search(src)
    while match is not None:
        closing_brace_index = find_matching(src, match.end(2), '{', '}') + match.end(2)
        src = f'{src[:match.start(1)]} {src[match.end(2):closing_brace_index]} {src[closing_brace_index+1:]}'
        match = if_re.search(src)
    return src
    
def replace_while_true(src):
    pass
    

with open('main.c', 'r') as inF:
    src = inF.read()

    src = replace_inner_while(src)
    # src = replace_while_break(src)
    # #print(src)
    src = drop_else(src)
    src = drop_if_less_than(src)
    src = replace_do_while(src)
    print(src)