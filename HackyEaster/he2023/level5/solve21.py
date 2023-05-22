def get_pos(l, pos):
    return l.split('_')[pos]

def uniqe_at_pos(lst, pos):
    hist = {}
    forbidden = set()
    for l in lst:
        l = l.split('_')
        for i in range(pos):
            forbidden.add(l[i])
        l = l[pos]
        if l in hist:
            hist[l] += 1
        else:
            hist[l] = 1
    s = {k for k, v in hist.items() if v == 1} - forbidden

    return [l for l in lst if get_pos(l, pos) in s]

with open('level5/singular_single_occurrences.txt', 'r') as inF:
    s = {l[:-2].split('{')[1] for l in inF}
    print(len(s))
    s = list(s)
    s0 = uniqe_at_pos(s, 0)
    print(len(s0))
    s1 = uniqe_at_pos(s0, 1)
    print(len(s1))
    s2 = uniqe_at_pos(s1, 2)
    print(len(s2))
    s3 = uniqe_at_pos(s2, 3)
    print(len(s3))
    print(s3)

    lengths = {}
    for l in s:
        if len(l) in lengths:
            lengths[len(l)] += 1
        else:
            lengths[len(l)] = 1
    print(lengths)

    for l in s:
        if len(l) == 25:
            print(l)