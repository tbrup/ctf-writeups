void main(void)

{
  byte bVar1;
  byte bVar2;
  byte bVar3;
  undefined uVar4;
  undefined uVar5;
  byte unaff_R1;
  byte bVar6;
  byte bVar7;
  byte bVar8;
  undefined2 uVar9;
  byte *pbVar10;
  byte bVar11;
  byte bVar12;
  undefined2 uVar13;
  int __denom;
  int __numer;
  byte bVar14;
  byte bVar15;
  undefined2 extraout_R23R22;
  undefined2 uVar16;
  byte extraout_Wlo;
  char extraout_Wlo_00;
  undefined2 uVar17;
  char cVar18;
  byte bVar19;
  byte *pbVar20;
  byte *pbVar21;
  byte *pbVar22;
  undefined2 unaff_Y;
  char cVar23;
  int iVar24;
  undefined *puVar25;
  char in_Cflg;
  bool bVar26;
  bool bVar27;
  char in_Hflg;
  char in_Tflg;
  char in_Iflg;
  div_t dVar28;
  undefined4 uVar29;
  undefined uStack0000;
  undefined auStack256 [255];
  undefined uStack1;
  
  uStack0000 = (undefined)unaff_Y;
  uStack1 = (undefined)((uint)unaff_Y >> 8);
  cVar18 = (char)((uint)auStack256 >> 8);
  cVar23 = cVar18 + -1;
  SREG = in_Cflg == '\x01' | (cVar23 == '\0') << 1 | (cVar23 < '\0') << 2 | (cVar18 == -0x80) << 3 |
         (cVar23 < '\0' != (cVar18 == -0x80)) << 4 | (in_Hflg == '\x01') << 5 |
         (in_Tflg == '\x01') << 6 | (in_Iflg == '\x01') << 7;

  Print::println("Santas Super Secret embedded Flag decrypt0r");
  uVar9 = CONCAT11(cVar18,0xff);
  __denom = CONCAT11(unaff_R1,0xd);
  uVar13 = 0;
  while( true ) {
    Print::println("Please login with user:password");
    Print::write("> ");
    pbVar22 = (byte *)CONCAT11(cVar23,0xff);
    pbVar10 = pbVar22;
    bVar8 = unaff_R1;
    while (((bVar8 != 0xd && (bVar8 != 10)) &&
           ((byte)uVar9 != (byte)pbVar10 ||
            (char)((uint)uVar9 >> 8) !=
            (char)((char)((uint)pbVar10 >> 8) + ((byte)uVar9 < (byte)pbVar10))))) {
      uVar17 = HardwareSerial::available((HardwareSerial *)Serial);
      bVar26 = unaff_R1 < (byte)uVar17;
      cVar18 = (char)((uint)uVar17 >> 8);
      if ((char)(unaff_R1 - (cVar18 + bVar26)) < '\0' !=
          (SBORROW1(unaff_R1,cVar18) != SBORROW1(unaff_R1 - cVar18,bVar26))) {
        HardwareSerial::read((HardwareSerial *)Serial);
        *pbVar10 = extraout_Wlo;
        pbVar10 = pbVar10 + 1;
        bVar8 = extraout_Wlo;
      }
    }

    // now the entered user:password is in the stack auStack256
    Print::println((char *)pbVar22);
    iVar24 = 0;
    __numer = 0;
    pbVar10 = logins;
    pbVar21 = pbVar22;
    do {
      pbVar20 = pbVar21 + 1;
      bVar14 = *pbVar21;
      pbVar21 = pbVar10 + 1;
      bVar8 = *pbVar10;
      *puVar25 = 0x1b;
      puVar25[-1] = 3;
      puVar25[-2] = 0;
      dVar28 = __divmodhi4(__numer,__denom);
      bVar19 = (byte)((ulong)dVar28 >> 0x10);
      bVar19 = *(byte *)CONCAT11((char)((ulong)dVar28 >> 0x18) - ((bVar19 < 0xb0) + -3),
                                 bVar19 + 0x50);
      if ((bVar14 ^ *(byte *)(CONCAT11(-((bVar19 < 0xcd) + -2),bVar19 + 0x33) + 0x25)) == bVar8) {
        iVar24 = iVar24 + 1;
      }
      bVar8 = (char)__numer + 1;
      cVar18 = (char)((uint)__numer >> 8) - (((char)__numer != -1) + -1);
      __numer = CONCAT11(cVar18,bVar8);
      pbVar10 = pbVar21;
      pbVar21 = pbVar20;
    } while (bVar8 != 0x21 || cVar18 != (byte)(unaff_R1 + (bVar8 < 0x21)));
    if (iVar24 == 0x21) break;
  }
  Print::println("Login Successful!");
  Print::println("Decrypting flag...");
  pEndFlag = (byte)pCurChar + 0x21;
  cVar20 = (char)((uint)pCurChar >> 8) + unaff_R1 + (0xde < (byte)pCurChar);
  pFlagChar = flags;

  while ((byte)pCurChar != pEndFlag ||
         (char)((uint)pCurChar >> 8) != (char)(cVar20 + ((byte)pCurChar < pEndFlag))) {

    HardwareSerial::write((HardwareSerial *)Serial,*pCurrChar ^ *pFlagChar);
    pFlagChar++
    pCurChar++
  }
  Print::println(&UNK_mem_0280);
  do {
                    /* WARNING: Do nothing block with infinite loop */
  } while( true );
}


