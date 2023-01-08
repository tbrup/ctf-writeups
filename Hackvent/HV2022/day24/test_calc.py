import itertools
import solve_day24
# from pwn import *
import pwn


IP = '152.96.7.2'
PORT = 5825

def test_calc():
    assert solve_day24.calc_block([0x01]) == 0x0100000001
    assert solve_day24.calc_block([0x0100]) == 0x010000000100
    assert solve_day24.calc_block([0x010000]) == 0x01000000010000
    assert solve_day24.calc_block([0x01000000]) == 0x0100000001000000


def test_bin_to_msg():
    for i in range(36):
        tb = (35-i)*b'\x00' + b'\x01' + i*b'\x00'
        tt = (35-i)*'00'    +  '01'   + i*'00'
        txt = solve_day24.bin_msg_to_txt(tb)
        assert txt == tt


def test_msg_to_bin():
    for i in range(36):
        tb = (35-i)*b'\x00' + b'\x01' + i*b'\x00'
        tt = (35-i)*'00'    +  '01'   + i*'00'
        msg = solve_day24.txt_msg_to_bin(tt)
        assert msg == tb


def test_bytes_to_seg():
    window = (1<<64)
    u = 0x11
    for _ in range(72):
        uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
        segs = solve_day24.bytes_to_seg(uBytes)
        utmp = solve_day24.seg_to_u(segs)
        assert utmp == u
        u *= 0x100
        

def test_seg_to_u():
    window = (1<<64)
    u = 0x11
    for _ in range(72):
        uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
        seg = solve_day24.bytes_to_seg(uBytes)
        uTmp = solve_day24.seg_to_u(seg)
        assert uTmp == u
        u *= 0x100

        
def test_seg_to_vseg():
    window = (1<<64)
    u = 0x11
    for _ in range(72):
        uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
        segs = solve_day24.bytes_to_seg(uBytes)
        vsegs = solve_day24.seg_to_vseg(segs)
        for (i, vs) in enumerate(vsegs):
            s = solve_day24.calc_block(vs)
            assert segs[i] == s
        u *= 0x100

        
def test_vseg_to_u():
    window = (1<<64)
    u = 0x11
    for _ in range(72):
        uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
        seg = solve_day24.bytes_to_seg(uBytes)
        vseg = solve_day24.seg_to_vseg(seg)
        seg1 = solve_day24.vseg_to_seg(vseg)
        uTmp = solve_day24.seg_to_u(seg1)
        assert uTmp == u
        u *= 0x100

        
def test_bseg_to_msg():
    u = 0x11
    for _ in range(72):
        uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
        segs = solve_day24.bytes_to_seg(uBytes)
        v_seg = solve_day24.seg_to_vseg(segs)
        b_seg = solve_day24.vseg_to_bseg(v_seg)

        msg = solve_day24.bseg_to_msg(b_seg)
        bs = solve_day24.msg_to_bseg(msg)
        
        assert bs == b_seg
        u *= 0x100
    


def test_msg_to_bseg():
    msg = b''
    for i in range(72):
        msg += i.to_bytes(1, 'little')

    b_segs = solve_day24.msg_to_bseg(msg)

    assert b_segs[0] == [ 0,  9, 18, 27, 36, 45, 54, 63]
    
    m2 = solve_day24.bseg_to_msg(b_segs)
    assert msg == m2


def test_simple_hash():
    msg = b'\x00'*35 + b'\x11'
    u = 0x1100000011

    uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
    hashed = solve_day24.hash2(msg)
    assert hashed == uBytes

    msg = b'\x00'*(35+36) + b'\x11'
    hashed = solve_day24.hash2(msg)
    assert hashed == uBytes

    msg1 = solve_day24.reverse_hash2(u)
    hashed2 = solve_day24.hash2(msg1)
    assert hashed == hashed2


def test_intermediates():
    for u in [0x11, 0x1234, 0x123456, 0x12345678, 0x1234567890, 0x1234567890ab,
    0x1234567890abcd, 0x1234567890abcdef]:
        uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
        msg = solve_day24.reverse_hash2(u)
        hashed = solve_day24.hash2(msg)
        uTmp = int.from_bytes(hashed, 'little')
        
        # now we have all the data for a round trip

        h2b_segs = solve_day24.msg_to_bseg(msg)
        h2v_segs = solve_day24.bseg_to_vseg(h2b_segs)
        h2s_segs = solve_day24.vseg_to_seg(h2v_segs)
        h2digest = solve_day24.sseg_to_bits(h2s_segs)

        r2s_segs = solve_day24.bytes_to_seg(hashed[::-1])
        r2v_segs = solve_day24.seg_to_vseg(r2s_segs)
        r2b_segs = solve_day24.vseg_to_bseg(r2v_segs)
        r2msg = solve_day24.bseg_to_msg(r2b_segs)
        
        assert h2digest == hashed
        assert r2s_segs == h2s_segs
        assert r2v_segs == h2v_segs
        assert r2b_segs == h2b_segs
    

def test_hash():
    u = 0x11
    for _ in range(72):
        msg = solve_day24.reverse_hash2(u)
        hashed = solve_day24.hash2(msg)
        uTmp = int.from_bytes(hashed, 'little')
        
        assert uTmp == u
        uBytes = u.to_bytes(solve_day24.HB_COUNT*8, 'little')
        # msg = solve_day24.reverse_hash(u)
        # msg2 = solve_day24.reverse_hash2(u)
        # hashed = solve_day24.hash(msg)
        # hashed2 = solve_day24.hash2(msg)
        # assert hashed == hashed2
        #
        # uTmp = int.from_bytes(hashed[::-1], 'little')
        # msg10 = solve_day24.reverse_hash2(uTmp)
        # hashed10 = solve_day24.hash2(msg10)
        # assert hashed10 == msg10
        #
        # hashed = solve_day24.hash(msg2)
        # hashed2 = solve_day24.hash2(msg2)
        # assert hashed == hashed2
        # assert hashed == uBytes
        # assert hashed2 == uBytes
        u *= 0x100


def test_v():
    for u, _ in itertools.product(range(0x100), range(8)):
        v1,v2 = solve_day24.calc_vs(u)
        u_new = solve_day24.calc_block([v1,v2])
        assert u == u_new
        u *= 0x100


def test_simple_u_sig():
    p = pwn.remote(IP, PORT)
    n, e, prime, nrg = solve_day24.getNEP(p)
    u = 0x1100000011
    for _ in range(9):
        for _ in range(4):
            msg = solve_day24.reverse_hash2(u)
            # t = solve_day24.bin_msg_to_txt(msg)
            _, sig, nrg = solve_day24.getSig(p, u, nrg)
            uNet = solve_day24.decode_sig(int(sig,16), n, e)
            hashed = solve_day24.hash2(msg)
            print(f'u_net: {uNet:0144x}')
            uByts = uNet.to_bytes(solve_day24.HB_COUNT*8, 'little')
            assert uByts == hashed
            assert u == uNet
            u *= 0x100
        u *= 0x100000000
    p.close()
            

def test_u_sig():
    p = pwn.remote(IP, PORT)

    n, e, prime, energy = solve_day24.getNEP(p)

    u = 0x11
    for _ in range(72):
        msg = solve_day24.reverse_hash2(u)
        # t = solve_day24.bin_msg_to_txt(msg)
        _, sig, energy = solve_day24.getSig(p, u, energy)
        uNet = solve_day24.decode_sig(int(sig,16), n, e)
        hashed = solve_day24.hash2(msg)
        print(f'u_net: {uNet:0144x}')
        uByts = uNet.to_bytes(solve_day24.HB_COUNT*8, 'little')
        assert uByts == hashed
        # assert u == uNet
        u *= 0x100
    p.close()


def test_msg_sig():
    p = pwn.remote(IP, PORT)

    n, e, prime, energy = solve_day24.getNEP(p)

    for i, x in itertools.product(range(72), range(256)):
        tx = f'{x:02x}'
        tt = i*'00' + tx

        _, sig, energy = solve_day24.getSigTxt(p, tt, energy)
        uNet = solve_day24.decode_sig(int(sig,16), n, e)
        print(f'u_net: {uNet:0144x}')
        tb = solve_day24.txt_msg_to_bin(tt)
        hashed = solve_day24.hash2(tb)
        uByts = uNet.to_bytes(solve_day24.HB_COUNT*8, 'little')
        if any(uByts[i] != hashed[i] for i in range(len(hashed))):
            print(uByts)
            print(hashed)
        assert uByts == hashed
    p.close()


def test_msg_sig22():
    p = pwn.remote(IP, PORT)
    n, e, prime, energy = solve_day24.getNEP(p)

    for i in range(36):
        for j in range(i,36):
            tt = i*'00' + 'c5' 
            if i != j:
                tt += j*'00' + '01'

            _, sig, energy = solve_day24.getSigTxt(p, tt, energy)
            uNet = solve_day24.decode_sig(int(sig,16), n, e)
            print(f'u_net: {uNet:0144x}')
            tb = solve_day24.txt_msg_to_bin(tt)
            hashed = solve_day24.hash2(tb)
            uByts = uNet.to_bytes(solve_day24.HB_COUNT*8, 'little')
            if any(uByts[i] != hashed[i] for i in range(len(hashed))):
                print(uByts)
                print(hashed)
            assert uByts == hashed
    p.close()


if __name__ == '__main__':
    test_bytes_to_seg()
    test_seg_to_u()
    test_seg_to_vseg()
    test_vseg_to_u()
    test_bseg_to_msg()
    test_msg_to_bseg()
    test_intermediates()
    test_hash()
    test_simple_hash()
    test_calc()
    test_v()
    test_msg_to_bin()
    test_bin_to_msg()
    test_simple_u_sig()
    test_u_sig()
    # test_hash()
