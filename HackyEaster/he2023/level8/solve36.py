"""
The Little Rabbit Ohaal

626b34041c11143a444e1b342c0e341036592d39044a0c102505145b57030c1b0e15290a533231071f71040465221023026b
7a2a304a14115a311d5b4d3d320e66520a11392e124a1000621a414310014e070245350f147431150a7105142273103a4328132f01181e
733e334a0615513203170a263d1632100f506c3f1d18461c2015554316074e1f1c47264c257427061f71080a2273103a4328043c47
626b2b081412463144411e733e0574004b0237280d5b09393315004103050f2a5d6a240943272513592c4a142373153c11670534050d1e
"""
import base64
import string

line = [
    "626b34041c11143a444e1b342c0e341036592d39044a0c102505145b57030c1b0e15290a533231071f71040465221023026b",
    "7a2a304a14115a311d5b4d3d320e66520a11392e124a1000621a414310014e070245350f147431150a7105142273103a4328132f01181e",
    "733e334a0615513203170a263d1632100f506c3f1d18461c2015554316074e1f1c47264c257427061f71080a2273103a4328043c47",
    "626b2b081412463144411e733e0574004b0237280d5b09393315004103050f2a5d6a240943272513592c4a142373153c11670534050d1e"]

lb = [base64.b16decode(l, True) for l in line]
crib = [ord(c) for c in "he2023{"]
crib =b'Enoovg'
crib =b'enoovg'
crib = [ord(c) for c in "ohaal"]
crib = b' gur'
crib = b' qbja' # ' down'
crib = b' vf gur'
crib = b' bhg bs ' # ' out of '
crib = b'} vf gur_' # '} is the '
crib = b' va gu'
crib = b"s ur2023{pe"
crib = b' nyy bs uvz '
crib = b"s ur2023{pe1"
crib = b'g guvat va gur '
crib = b"s ur2023{pe1o_"
crib = b' yvggyr Ohaal jvgu'
crib = b' svefg guvat va gur zbeavat'
crib = b' jbaqre vs ur2023{pe1o_qe4ttva'
crib = b' gur svefg guvat va gur zbeavat '
crib = b'V unir n yvggyr Ohaal jvgu n pbng '
crib = b'Naq arneyl nyy bs uvz vf juvgr rkprcg '
crib = b'V unir n yvggyr Ohaal jvgu n pbng nf fbsg '
crib = b'V jbaqre vs ur2023{pe1o_qe4ttva_4_ce0svg!} '
crib = b'Gur svefg guvat va gur zbeavat jura V trg bhg '
crib = b'V unir n yvggyr Ohaal jvgu n pbng nf fbsg nf qbja'
crib = b'V jbaqre vs ur2023{pe1o_qe4ttva_4_ce0svg!} vf gur'
crib = b" ur2023{"

last = len(lb[0]) - len(crib)

# take a crib, apply it to the first line and get the pad, then use this pad to get the result for the other lines
def use_crib_line(lb, iLine, crib, pos):
    charset = string.ascii_letters + string.digits + ' {},.!_?' 
    # charset = string.printable
    pad = [(crib[i] ^ lb[iLine][pos+i]) & 0xFF for i in range(len(crib))]
    clear = []
    for j in range(len(lb)):
        tmp = ''.join(chr(pad[i] ^ lb[j][pos+i]) for i in range(len(pad)))
        if all(c in charset for c in tmp):
            clear.append(tmp)
    return clear, pad


for iLine in range(4):
    for pos in range(last):
        clear,pad = use_crib_line(lb, iLine, crib, pos)
        if len(clear) == 4:
            # print(f"{crib} {''.join(chr(c) for c in pad)}: pos: {pos} ", end='')
            print(f"{crib} pos: {pos} ", end='')
            for c in clear:
                print(f",{c}, ", end='')
            print()
        
# def find_next(lb, )