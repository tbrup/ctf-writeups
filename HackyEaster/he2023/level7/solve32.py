def MOD(n1,n2):
    return n1 % n2

def CHAR(n):
    try:
        return chr(n)
    except Exception:
        return ' '

E2=5
F2=4
J6=2
B7=9
D14=7
G14=8

def kaos(E2,F2,J6,B7,D14,G14):
    F12=MOD(E2*B7+D14,64)
    C3=(J6+B7+34+G14)%64
    H3=(B7*J6*7)%64
    B13=MOD(B7*J6*G14+5,64)
    F4=(E2*G14+D14+J6)%64
    D5=(E2+J6+B7+D14+G14)%64
    J13=MOD(D14+B7*E2,64)
    I5=(H3+D5)%64
    G6=MOD(G14*B7+D14,64)
    C6=MOD(H3+G6+B13+3,64)
    D11=MOD(E2*G14,64)

    J3=(F12+D11+D5+F4)%64
    I7=MOD(F12+D11*G6+H3,64)
    F10=MOD(J13+F12+D11+F4+17,64)
    I10=MOD(J6*G14+B7,64)
    B5=(J13+D11+F12+I10)%64
    E6=MOD(F4+D11+I10,64)
    H11=MOD(C3+H3+F12,64)
    C12=MOD(B13+F12+I10,64)
    H13=MOD(H3+G6+F12+D11+B13+B13,64)

    # G4=D2
    # J4=J14
    # H5=J14
    # I6=J14
    # H7=J14
    # G11=D2
    # D12=D2
    # E12=J14
    # H12=J14
    # F13=J14
    # D13=J14


    ## OUTPUT???
    B8=CHAR(52+B5)
    C8=CHAR(44+I7)
    D8=CHAR(48+J3)
    E8=CHAR(45+E6)
    F8=CHAR(42+I5)
    G8=CHAR(63-F10)
    H8=CHAR(H13+93)
    I8=CHAR(C12+68)
    J8=CHAR(H13+74)
    B9=CHAR(I7-5)
    C9=CHAR(C6*6+2)
    D9=CHAR(I7+B5+J6-34)
    E9=CHAR(91-C12)
    F9=CHAR(I7+H11-10)
    G9=CHAR(B5-4)
    H9=CHAR(H11+H13+I5+J3)
    I9=CHAR(H13+E6)
    J9=CHAR(E6*H11-25)
    return B8+C8+D8+E8+F8+G8+H8+I8+J8+B9+C9+D9+E9+F9+G9+H9+I9+J9


import itertools
for n1, n2 in itertools.product(range(10), range(10)):
    for n3, n4, n5, n6 in itertools.product(range(10), range(10), range(10), range(10)):
        flag = kaos(n1,n2,n3,n4,n5,n6)
        if flag[:6] == "he2023":
            print(n1,n2,n3,n4,n5,n6)
            print(flag)
            exit()
    print(n1,n2)
