# sift through a list of passwords, calculate sha-1 and compare with a given
import hashlib
import fileinput
import sys


def sift(target, fn):
    index = 1
    with open(fn, 'rb') as pw_file:
        with open('hashes.txt', 'w') as hash_file:
            for l in pw_file:
                try:
                    pw = l.strip()
                    sha = hashlib.sha1()
                    sha.update(pw)
                    hsh = sha.hexdigest()
                    if target in hsh:
                        # hash_file.write(f'{pw} - {sha.hexdigest()}\n')
                        print(f'{pw} - {sha.hexdigest()}')
                    if index % 1000000 == 0:
                        print(f'{target} -- index is {index // 1000000} M')
                    index += 1
                except UnicodeDecodeError:
                    print(l)


def siftStdin(target):
    for index, l in enumerate(sys.stdin.buffer.readlines(), start=1):
        pw = l.rstrip()
        sha = hashlib.sha1()
        sha.update(pw)
        hsh = sha.hexdigest()
        if target in hsh:
            # hash_file.write(f'{pw} - {sha.hexdigest()}\n')
            print(f'{pw} - {sha.hexdigest()}')
        if index % 1000000 == 0:
            print(f'{target} -- index is {index}')


if __name__ == '__main__':
    target = '69792b677e3e4c7a6d78545c205c4e5e26'
    crib = ''.join(chr(int(target[i:i + 2], 16)) for i in range(0, len(target), 2))
    print(crib)
    crackstation = ''
    crackstation += f'{ord("4"):02x}{ord("L"):02x}{ord("t"):02x}'
    print(crackstation + target)
    # sift('69792b677e3e4c7a6d78545c205c4e5e26', 'crackstation.txt')
    # siftStdin('69792b677e3e4c7a6d78545c205c4e5e26')
    # sift('69792b677e3e4c7a6d78545c205c4e5e26', '/Users/thomasbrupbacher/Downloads/rockyou.txt')
