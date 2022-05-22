
def diff(l1, l2):
    retVal = []
    for p1 in l1:
        for p2 in l2:
            retVal.append(p1-p2)

    return retVal


def printDiffs(msg, crib):
    for i in range(len(crib)-1):
        tmp = sorted(diff(pos[crib[i]], pos[crib[i+1]]))
        print(crib[i], pos[crib[i]])
        print(crib[i+1], pos[crib[i+1]])
        print(tmp)


msg = '21{_inake0dltn_2olospena__iht_fthet!}'

pos = {}
for i in range(len(msg)):
    if msg[i] in pos.keys():
        pos[msg[i]].append(i)
    else:
        pos[msg[i]] = [i]

for k in sorted(pos.keys()):
    print(k, pos[k])

crib = 'he2021{'
crib2 = 'snake'
print(len(msg))

printDiffs(msg, crib)
printDiffs(msg, crib2)

