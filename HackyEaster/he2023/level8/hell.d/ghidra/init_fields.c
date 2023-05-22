
void init_fields(void)

{
  int iVar1;
  uint unaff_EBX;
  int local_1c;
  
  iVar1 = 0x62f83d1b;
  while( true ) {
    do {
      while( true ) {
        do {
          while( true ) {
            do {
              while( true ) {
                do {
                  while( true ) {
                    do {
                      while( true ) {
                        do {
                          while( true ) {
                            do {
                              while( true ) {
                                do {
                                  while (iVar1 == 0x7faf7d51) {
                                    *(char *)((ulong)(byte)(&DAT_00108020)[local_1c] +
                                             (long)DAT_00108840) = (char)local_1c;
                                    local_1c = local_1c + 1;
                                    iVar1 = 0x1cb758be;
                                  }
                                } while (0x7faf7d51 < iVar1);
                                if (iVar1 != 0x7803232e) break;
                                iVar1 = 0x18364c28;
                                if (local_1c < 0x40) {
                                  iVar1 = 0x52c36d87;
                                }
                              }
                            } while (0x7803232e < iVar1);
                            if (iVar1 != 0x62f83d1b) break;
                            unaff_EBX = DAT_0010883c * (DAT_0010883c + 1);
                            iVar1 = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838) & 0xf6650a0c)
                                    + 0x39766225;
                          }
                        } while (0x62f83d1b < iVar1);
                        if (iVar1 != 0x52c36d87) break;
                        iVar1 = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838) & 0xb85d99b3) +
                                0x7faf7d51;
                      }
                    } while (0x52c36d87 < iVar1);
                    if (iVar1 != 0x39766225) break;
                    DAT_00108840 = malloc(0x100);
                    local_1c = 0;
                    iVar1 = 0x1cb758be;
                  }
                } while (0x39766225 < iVar1);
                if (iVar1 != 0x380d1704) break;
                iVar1 = 0x52c36d87;
              }
            } while (0x380d1704 < iVar1);
            if (iVar1 != 0x2fdb6c31) break;
            iVar1 = 0x62f83d1b;
          }
        } while (0x2fdb6c31 < iVar1);
        if (iVar1 != 0x2265dca6) break;
        iVar1 = 0x1cb758be;
      }
    } while (0x2265dca6 < iVar1);
    if (iVar1 == 0x18364c28) break;
    if (iVar1 == 0x1cb758be) {
      iVar1 = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838) & 0xaa62b978) + 0x7803232e;
    }
  }
  return;
}

