void burp(int param_1)

{
  int eax;
  uint unaff_EBX;
  int local_2c;
  code *local_20;
  
  eax = 0x1999de95;
  local_2c = param_1;
  while( true ) {
    do {
      while( true ) {
        do {
          while( true ) {
            do {
              while (eax == 0x7f67ce67) {
                eax = 0xc3de320;
              }
            } while (0x7f67ce67 < eax);
            if (eax != 0x7d59fadb) break;
            eax = 0x3e128c3b;
          }
        } while (0x7d59fadb < eax);
        if (eax != 0x648831e2) break;
        (*local_20)(0);
        eax = 0x4f59043e;
      }
    } while (0x648831e2 < eax);
    if (eax == 0x4f59043e) break;
    if (eax < 0x4f59043f) {
      if (eax == 0x3e128c3b) {
        eax = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838) & 0x45ae8a3e) + 0x37ab709d;
      }
      else if (eax < 0x3e128c3c) {
        if (eax == 0x3dc94629) {
          local_20 = (code *)dlsym(0xffffffffffffffff,&s_exit);
          eax = (-(uint)(local_20 == (code *)0x0) & 0x36101e57) + 0x8026de4;
        }
        else if (eax < 0x3dc9462a) {
          if (eax == 0x37ab709d) {
            printf("Burp...");
            local_2c = -1;
            eax = 0x8026de4;
          }
          else if (eax < 0x37ab709e) {
            if (eax == 0x3086084a) {
              eax = 0x8026de4;
            }
            else if (eax < 0x3086084b) {
              if (eax == 0x23191abe) {
                eax = 0x1999de95;
              }
              else if (eax < 0x23191abf) {
                if (eax == 0x1999de95) {
                  unaff_EBX = DAT_0010883c * (DAT_0010883c + 1);
                  eax = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838) & 0x1a6b5284) + 0x8adc83a
                  ;
                }
                else if (eax < 0x1999de96) {
                  if (eax == 0xc3de320) {
                    eax = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838) & 0x419e883e) +
                          0x3dc94629;
                  }
                  else if (eax < 0xc3de321) {
                    if (eax == 0x8026de4) {
                      eax = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838) & 0xcbfdd668) +
                            0x648831e2;
                    }
                    else if ((eax == 0x8adc83a) && (eax = 0x4f59043e, local_2c == 0xe)) {
                      eax = 0xc3de320;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  return;
}

