
undefined4 main(void)

{
  byte bVar1;
  int eax;
  uint uVar2;
  uint uVar3;
  int iVar4;
  size_t sVar5;
  uint unaff_EBX;
  uint unaff_R12D;
  uint unaff_R13D;
  uint unaff_R14D;
  uint unaff_R15D;
  long in_FS_OFFSET;
  uint local_24c;
  uint local_248;
  uint local_244;
  uint local_240;
  uint local_23c;
  uint local_238;
  uint local_234;
  uint local_230;
  undefined4 local_22c;
  uint local_228;
  uint local_224;
  uint local_220;
  uint local_21c;
  uint local_218;
  uint local_214;
  uint local_210;
  uint local_20c;
  uint local_200;
  byte local_1f4;
  byte local_1ef;
  byte local_1e6;
  byte local_1e3;
  ushort local_1e2;
  int local_1e0;
  int local_1d8;
  int local_1d0;
  int local_1c4;
  int local_190;
  int local_15c;
  int local_150;
  int local_148;
  int local_140;
  int local_dc;
  ulong len_bin_data;
  char *user_input;
  code *local_c8;
  ulong local_c0;
  size_t user_input_len;
  long local_b0;
  code *local_a8;
  code *local_a0;
  code *local_98;
  code *local_90;
  code *local_88;
  code *local_80;
  code *local_78;
  code *local_70;
  code *local_68;
  code *local_60;
  code *local_58;
  char *local_50;
  char *user_input_ptr;
  
  eax = 0x1b3a0df2;
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
                                  while( true ) {
                                    do {
                                      while (eax == 0x7ef1a99f) {
                                        eax = 0x1fab566;
                                      }
                                    } while (0x7ef1a99f < eax);
                                    if (eax != 0x670d50aa) break;
                                    user_input_len = 0;
                                    len_bin_data = 0;
                                    init_stdio();
                                    setup_signals();
                                    puts("Welcome to....");
                                    puts(
                                        "      :^^.         .^^:      ..:^^::.       :::              .::.                \n      !??!         .777    .^!?YYJ7!! ~:     ~!!             :!!:                \n      !77J.         :7!?:   !7?#&G5?^^!!.    ~!~             :~~^                 \n      !77Y:        :!!?:   ?JY&BJ7!~~!?^    ~!~.             :~~^                \n     .!!!7!~~~~~~~~!!!?:   !JJ! .^~~~!YB~    ^~~.            .~~^                \n     .!!7 JJJJJJJJJY?!!?.    .. ^5Y?!~~!^    ^~~.            .^^^                 \n     :!!?5555555555?~~?.    .  ^P5J!^^~~.   ^~~ .            .^^^                \n     :!!?J^^^^^^^^^~~~?.   .~~:  ^::::^^~:   ^^^.            .^^^                \n      :~~J7         ^~~?    ^~~^:...:^~?G~   :^^::::::::::.  .:: ::..........     \n     ^??Y!         !???    :^~!!77?J5#@B:    !?7777777777?~  .!777777777777^     \n     .Y55~          ~55?     :~7JY5PB##P^    J555555555555^  :Y55555555555Y.      \n      :~~.         .~~^      .:~!777~:      ^~~~~~~~~~~~~ .  .~~~~~~~~~~~~:      \n"
                                        );
                                    puts(
                                        "Entrance free, it\'s just the flag that will cost your sani ty!"
                                        );
                                    puts(
                                        "=========================================================== ===================="
                                        );
                                    user_input = (char *)malloc(0x100);
                                    fgets(user_input,0x100,stdin);
                                    sVar5 = strcspn(user_input,"\n");
                                    user_input[sVar5] = '\0';
                                    user_input_len = strlen(user_input);
                                    user_input_ptr = user_input;
                                    eax = 0x5cced497;
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
                                                            while (eax == 0x67f9bce3) {
                                                              local_dc = 0;
                                                              eax = 0x4f2b5ebb;
                                                            }
                                                          } while (0x67f9bce3 < eax);
                                                          if (eax != 0x5eda4e7a) break;
                                                          eax = 0x4f2b5ebb;
                                                        }
                                                      } while (0x5eda4e7a < eax);
                                                      if (eax != 0x5cced497) break;
                                                      local_228 = DAT_0010883c * (DAT_0010883c + 1);
                                                      eax = (-(uint)((local_228 & 1) != 0 &&
                                                                    9 < DAT_00108838) & 0xe3d46c4b)
                                                            + 0x67f9bce3;
                                                    }
                                                  } while (0x5cced497 < eax);
                                                  if (eax != 0x53825296) break;
                                                  eax = 0x3ee9cef4;
                                                  if (local_dc < (int)user_input_len) {
                                                    eax = 0xc3fd678;
                                                  }
                                                }
                                              } while (0x53825296 < eax);
                                              if (eax != 0x4f2b5ebb) break;
                                              eax = (-(uint)((local_228 & 1) != 0 &&
                                                            9 < DAT_00108838) & 0xb57fbe4) +
                                                    0x53825296;
                                            }
                                          } while (0x4f2b5ebb < eax);
                                          if (eax != 0x4bce292e) break;
                                          eax = 0x5cced497;
                                        }
                                      } while (0x4bce292e < eax);
                                      if (eax == 0x3ee9cef4) break;
                                      if (eax < 0x3ee9cef5) {
                                        if (eax == 0x2bda6101) {
                                          eax = 0xc3fd678;
                                        }
                                        else if (eax < 0x2bda6102) {
                                          if (eax == 0xc3fd678) {
                                            eax = (-(uint)((local_228 & 1) != 0 && 9 < DAT_00108838)
                                                  & 0x50e7736) + 0x26cbe9cb;
                                          }
                                          else if (eax == 0x26cbe9cb) {
                                            user_input[local_dc] = user_input[local_dc] + -0xd;
                                            local_dc = local_dc + 1;
                                            eax = 0x4f2b5ebb;
                                          }
                                        }
                                      }
                                    }
                                    local_50 = user_input;
                                    eax = 0x46088970;
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
                                                                    while (eax == 0x73de90e5) {
                                                                      eax = 0x2fe68dc3;
                                                                    }
                                                                  } while (0x73de90e5 < eax);
                                                                  if (eax != 0x6ab7ee55) break;
                                                                  eax = (-(uint)((unaff_R14D & 1) !=
                                                                                 0 && 9 < 
                                                  DAT_00108838) & 0xb241c98a) + 0x73de90e5;
                                                  }
                                                  } while (0x6ab7ee55 < eax);
                                                  if (eax != 0x645455cd) break;
                                                  eax = 0x46088970;
                                                  }
                                                  } while (0x645455cd < eax);
                                                  if (eax != 0x6137b2a9) break;
                                                  eax = 0x2fe68dc3;
                                                  }
                                                  } while (0x6137b2a9 < eax);
                                                  if (eax != 0x612a21e0) break;
                                                  eax = (-(uint)((unaff_R14D & 1) != 0 &&
                                                                9 < DAT_00108838) & 0x2d09ae3e) +
                                                        0x17e599df;
                                                  }
                                                  } while (0x612a21e0 < eax);
                                                  if (eax != 0x5a49acc3) break;
                                                  local_1e3 = 0;
                                                  eax = 0x612a21e0;
                                                }
                                              } while (0x5a49acc3 < eax);
                                              if (eax != 0x59b482ee) break;
                                              eax = (-(uint)((unaff_R14D & 1) != 0 &&
                                                            9 < DAT_00108838) & 0x704e) + 0xca07e9d;
                                            }
                                          } while (0x59b482ee < eax);
                                          if (eax != 0x4f6bb466) break;
                                          bVar1 = 0x15;
                                          eax = 0x61c7fa04;
                                          while (eax != 0x7fa1ebe8) {
                                            if (eax < 0x7fa1ebe9) {
                                              if (eax == 0x61c7fa04) {
                                                eax = (-(uint)(((DAT_0010883c + 1) * DAT_0010883c &
                                                               1U) != 0 && 9 < DAT_00108838) &
                                                      0xcf2bf30f) + 0x5490b56f;
                                              }
                                              else if (eax < 0x61c7fa05) {
                                                if (eax == 0x23bca87e) {
                                                  eax = 0x61c7fa04;
                                                }
                                                else if (eax == 0x5490b56f) {
                                                  bVar1 = (bVar1 ^ 0xe0) & bVar1;
                                                  uVar2 = *(uint *)(user_input + local_1e3) << bVar1
                                                  ;
                                                  uVar3 = *(uint *)(user_input + local_1e3) >>
                                                          ((~-bVar1 ^ 0x1f) & 0x1f);
                                                  local_248 = uVar2 & uVar3 | uVar3 ^ uVar2;
                                                  eax = 0x7fa1ebe8;
                                                }
                                              }
                                            }
                                          }
                                          *(uint *)(user_input + local_1e3) = local_248;
                                          eax = 0x140e1fc8;
                                        }
                                      } while (0x4f6bb466 < eax);
                                      if (eax == 0x4b069874) break;
                                      if (eax < 0x4b069875) {
                                        if (eax == 0x46088970) {
                                          unaff_R14D = DAT_0010883c * (DAT_0010883c + 1);
                                          eax = (-(uint)((unaff_R14D & 1) != 0 && 9 < DAT_00108838)
                                                & 0xa0aa90a) + 0x5a49acc3;
                                        }
                                        else if (eax < 0x46088971) {
                                          if (eax == 0x44ef481d) {
                                            eax = 0x612a21e0;
                                          }
                                          else if (eax < 0x44ef481e) {
                                            if (eax == 0x2fe68dc3) {
                                              eax = (-(uint)((unaff_R14D & 1) != 0 &&
                                                            9 < DAT_00108838) & 0x11cbfe43) +
                                                    0x4f6bb466;
                                            }
                                            else if (eax < 0x2fe68dc4) {
                                              if (eax == 0x26205a6f) {
                                                eax = 0x6ab7ee55;
                                              }
                                              else if (eax < 0x26205a70) {
                                                if (eax == 0x17e599df) {
                                                  eax = (-(uint)((ulong)local_1e3 <
                                                                (long)(int)user_input_len - 4U) &
                                                        0x1fb155e1) + 0x4b069874;
                                                }
                                                else if (eax < 0x17e599e0) {
                                                  if (eax == 0x17970726) {
                                                    local_1e3 = local_1e3 + 4;
                                                    eax = 0x612a21e0;
                                                  }
                                                  else if (eax < 0x17970727) {
                                                    if (eax == 0x140e1fc8) {
                                                      eax = (-(uint)((unaff_R14D & 1) != 0 &&
                                                                    9 < DAT_00108838) & 0xee704d0f)
                                                            + 0x17970726;
                                                    }
                                                    else if (eax < 0x140e1fc9) {
                                                      if (eax == 0xca0eeeb) {
                                                        eax = 0x59b482ee;
                                                      }
                                                      else if (eax < 0xca0eeec) {
                                                        if (eax == 0x6075435) {
                                                          eax = 0x140e1fc8;
                                                        }
                                                        else if (eax == 0xca07e9d) {
                                                          bVar1 = 0x15;
                                                          eax = 0x8eafe17;
                                                          do {
                                                            while( true ) {
                                                              do {
                                                                while( true ) {
                                                                  do {
                                                                    while (eax == 0x5daba1af) {
                                                                      bVar1 = (bVar1 ^ 0xe0) & bVar1
                                                                      ;
                                                                      uVar2 = *(uint *)(user_input +
                                                                                       local_1e3) >>
                                                                              bVar1;
                                                                      uVar3 = *(uint *)(user_input +
                                                                                       local_1e3) <<
                                                                              ((~-bVar1 ^ 0x1f) &
                                                                              0x1f);
                                                                      local_24c = uVar2 & uVar3 |
                                                                                  uVar3 ^ uVar2;
                                                                      eax = 0x3c12c96a;
                                                                    }
                                                                  } while (0x5daba1af < eax);
                                                                  if (eax != 0x463175c6) break;
                                                                  eax = 0x8eafe17;
                                                                }
                                                              } while (0x463175c6 < eax);
                                                              if (eax != 0x8eafe17) break;
                                                              eax = (-(uint)(((DAT_0010883c + 1) *
                                                                              DAT_0010883c & 1U) !=
                                                                             0 && 9 < DAT_00108838)
                                                                    & 0xe885d417) + 0x5daba1af;
                                                            }
                                                          } while (eax != 0x3c12c96a);
                                                          *(uint *)(user_input + local_1e3) =
                                                               local_24c;
                                                          eax = 0x140e1fc8;
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
                                    }
                                    local_c8 = (code *)decode_base64_input(user_input,user_input_len
                                                                           ,&len_bin_data);
                                    eax = (int)len_bin_data;
                                    iVar4 = 0x46088970;
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
                                                                    while (iVar4 == 0x73de90e5) {
                                                                      iVar4 = 0x59b482ee;
                                                                    }
                                                                  } while (0x73de90e5 < iVar4);
                                                                  if (iVar4 != 0x6ab7ee55) break;
                                                                  iVar4 = (-(uint)((unaff_R13D & 1)
                                                                                   != 0 && 9 < 
                                                  DAT_00108838) & 0xb241c98a) + 0x73de90e5;
                                                  }
                                                  } while (0x6ab7ee55 < iVar4);
                                                  if (iVar4 != 0x645455cd) break;
                                                  iVar4 = 0x46088970;
                                                  }
                                                  } while (0x645455cd < iVar4);
                                                  if (iVar4 != 0x6137b2a9) break;
                                                  iVar4 = 0x2fe68dc3;
                                                  }
                                                  } while (0x6137b2a9 < iVar4);
                                                  if (iVar4 != 0x612a21e0) break;
                                                  iVar4 = (-(uint)((unaff_R13D & 1) != 0 &&
                                                                  9 < DAT_00108838) & 0x2d09ae3e) +
                                                          0x17e599df;
                                                  }
                                                  } while (0x612a21e0 < iVar4);
                                                  if (iVar4 != 0x5a49acc3) break;
                                                  local_1e6 = 0;
                                                  iVar4 = 0x612a21e0;
                                                }
                                              } while (0x5a49acc3 < iVar4);
                                              if (iVar4 != 0x59b482ee) break;
                                              iVar4 = (-(uint)((unaff_R13D & 1) != 0 &&
                                                              9 < DAT_00108838) & 0x704e) +
                                                      0xca07e9d;
                                            }
                                          } while (0x59b482ee < iVar4);
                                          if (iVar4 != 0x4f6bb466) break;
                                          bVar1 = 7;
                                          iVar4 = 0x61c7fa04;
                                          while (iVar4 != 0x7fa1ebe8) {
                                            if (iVar4 < 0x7fa1ebe9) {
                                              if (iVar4 == 0x61c7fa04) {
                                                iVar4 = (-(uint)(((DAT_0010883c + 1) * DAT_0010883c
                                                                 & 1U) != 0 && 9 < DAT_00108838) &
                                                        0xcf2bf30f) + 0x5490b56f;
                                              }
                                              else if (iVar4 < 0x61c7fa05) {
                                                if (iVar4 == 0x23bca87e) {
                                                  iVar4 = 0x61c7fa04;
                                                }
                                                else if (iVar4 == 0x5490b56f) {
                                                  bVar1 = (bVar1 ^ 0xe0) & bVar1;
                                                  uVar2 = *(uint *)(local_c8 + local_1e6) << bVar1;
                                                  uVar3 = *(uint *)(local_c8 + local_1e6) >>
                                                          ((~-bVar1 ^ 0x1f) & 0x1f);
                                                  local_240 = uVar2 & uVar3 | uVar3 ^ uVar2;
                                                  iVar4 = 0x7fa1ebe8;
                                                }
                                              }
                                            }
                                          }
                                          *(uint *)(local_c8 + local_1e6) = local_240;
                                          iVar4 = 0x140e1fc8;
                                        }
                                      } while (0x4f6bb466 < iVar4);
                                      if (iVar4 == 0x4b069874) break;
                                      if (iVar4 < 0x4b069875) {
                                        if (iVar4 == 0x46088970) {
                                          unaff_R13D = DAT_0010883c * (DAT_0010883c + 1);
                                          iVar4 = (-(uint)((unaff_R13D & 1) != 0 && 9 < DAT_00108838
                                                          ) & 0xa0aa90a) + 0x5a49acc3;
                                        }
                                        else if (iVar4 < 0x46088971) {
                                          if (iVar4 == 0x44ef481d) {
                                            iVar4 = 0x612a21e0;
                                          }
                                          else if (iVar4 < 0x44ef481e) {
                                            if (iVar4 == 0x2fe68dc3) {
                                              iVar4 = (-(uint)((unaff_R13D & 1) != 0 &&
                                                              9 < DAT_00108838) & 0x11cbfe43) +
                                                      0x4f6bb466;
                                            }
                                            else if (iVar4 < 0x2fe68dc4) {
                                              if (iVar4 == 0x26205a6f) {
                                                iVar4 = 0x6ab7ee55;
                                              }
                                              else if (iVar4 < 0x26205a70) {
                                                if (iVar4 == 0x17e599df) {
                                                  iVar4 = (-(uint)((ulong)local_1e6 < (long)eax - 4U
                                                                  ) & 0x1fb155e1) + 0x4b069874;
                                                }
                                                else if (iVar4 < 0x17e599e0) {
                                                  if (iVar4 == 0x17970726) {
                                                    local_1e6 = local_1e6 + 4;
                                                    iVar4 = 0x612a21e0;
                                                  }
                                                  else if (iVar4 < 0x17970727) {
                                                    if (iVar4 == 0x140e1fc8) {
                                                      iVar4 = (-(uint)((unaff_R13D & 1) != 0 &&
                                                                      9 < DAT_00108838) & 0xee704d0f
                                                              ) + 0x17970726;
                                                    }
                                                    else if (iVar4 < 0x140e1fc9) {
                                                      if (iVar4 == 0xca0eeeb) {
                                                        iVar4 = 0x59b482ee;
                                                      }
                                                      else if (iVar4 < 0xca0eeec) {
                                                        if (iVar4 == 0x6075435) {
                                                          iVar4 = 0x140e1fc8;
                                                        }
                                                        else if (iVar4 == 0xca07e9d) {
                                                          bVar1 = 7;
                                                          iVar4 = 0x8eafe17;
                                                          do {
                                                            while( true ) {
                                                              do {
                                                                while( true ) {
                                                                  do {
                                                                    while (iVar4 == 0x5daba1af) {
                                                                      bVar1 = (bVar1 ^ 0xe0) & bVar1
                                                                      ;
                                                                      uVar2 = *(uint *)(local_c8 +
                                                                                       local_1e6) >>
                                                                              bVar1;
                                                                      uVar3 = *(uint *)(local_c8 +
                                                                                       local_1e6) <<
                                                                              ((~-bVar1 ^ 0x1f) &
                                                                              0x1f);
                                                                      local_244 = uVar2 & uVar3 |
                                                                                  uVar3 ^ uVar2;
                                                                      iVar4 = 0x3c12c96a;
                                                                    }
                                                                  } while (0x5daba1af < iVar4);
                                                                  if (iVar4 != 0x463175c6) break;
                                                                  iVar4 = 0x8eafe17;
                                                                }
                                                              } while (0x463175c6 < iVar4);
                                                              if (iVar4 != 0x8eafe17) break;
                                                              iVar4 = (-(uint)(((DAT_0010883c + 1) *
                                                                                DAT_0010883c & 1U)
                                                                               != 0 && 9 < 
                                                  DAT_00108838) & 0xe885d417) + 0x5daba1af;
                                                  }
                                                  } while (iVar4 != 0x3c12c96a);
                                                  *(uint *)(local_c8 + local_1e6) = local_244;
                                                  iVar4 = 0x140e1fc8;
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
                                    }
                                    iVar4 = 0x20ab5d61;
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
                                                        while (iVar4 == 0x77dfeec7) {
                                                          iVar4 = (-(uint)((local_218 & 1) != 0 &&
                                                                          9 < DAT_00108838) &
                                                                  0xd7858fe2) + 0x6da5af8f;
                                                        }
                                                      } while (0x77dfeec7 < iVar4);
                                                      if (iVar4 != 0x6da5af8f) break;
                                                      iVar4 = 0x4f67f914;
                                                    }
                                                  } while (0x6da5af8f < iVar4);
                                                  if (iVar4 != 0x5b50b428) break;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                              } while (0x5b50b428 < iVar4);
                                              if (iVar4 != 0x55a2c4e1) break;
                                              iVar4 = 0x20ab5d61;
                                            }
                                          } while (0x55a2c4e1 < iVar4);
                                          if (iVar4 != 0x53bdf3fb) break;
                                          iVar4 = (-(uint)((local_218 & 1) != 0 && 9 < DAT_00108838)
                                                  & 0xd833a517) + 0x3e8b54a6;
                                        }
                                      } while (0x53bdf3fb < iVar4);
                                      if (iVar4 == 0x4f67f914) break;
                                      if (iVar4 < 0x4f67f915) {
                                        if (iVar4 == 0x452b3f71) {
                                          iVar4 = 0x77dfeec7;
                                        }
                                        else if (iVar4 < 0x452b3f72) {
                                          if (iVar4 == 0x436b958c) {
                                            iVar4 = 0x77dfeec7;
                                            if (local_140 < eax) {
                                              iVar4 = 0x53bdf3fb;
                                            }
                                          }
                                          else if (iVar4 < 0x436b958d) {
                                            if (iVar4 == 0x3e8b54a6) {
                                              local_c8[local_140] = (code)~(byte)local_c8[local_140]
                                              ;
                                              local_140 = local_140 + 1;
                                              iVar4 = 0x1feb2fd4;
                                            }
                                            else if (iVar4 < 0x3e8b54a7) {
                                              if (iVar4 == 0x20ab5d61) {
                                                local_218 = DAT_0010883c * (DAT_0010883c + 1);
                                                iVar4 = (-(uint)((local_218 & 1) != 0 &&
                                                                9 < DAT_00108838) & 0x358e8a57) +
                                                        0x20143a8a;
                                              }
                                              else if (iVar4 < 0x20ab5d62) {
                                                if (iVar4 == 0x20143a8a) {
                                                  local_140 = 0;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                                else if (iVar4 < 0x20143a8b) {
                                                  if (iVar4 == 0x16bef9bd) {
                                                    iVar4 = 0x53bdf3fb;
                                                  }
                                                  else if (iVar4 == 0x1feb2fd4) {
                                                    iVar4 = (-(uint)((local_218 & 1) != 0 &&
                                                                    9 < DAT_00108838) & 0x17e51e9c)
                                                            + 0x436b958c;
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                    iVar4 = 0x20ab5d61;
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
                                                        while (iVar4 == 0x77dfeec7) {
                                                          iVar4 = (-(uint)((local_214 & 1) != 0 &&
                                                                          9 < DAT_00108838) &
                                                                  0xd7858fe2) + 0x6da5af8f;
                                                        }
                                                      } while (0x77dfeec7 < iVar4);
                                                      if (iVar4 != 0x6da5af8f) break;
                                                      iVar4 = 0x4f67f914;
                                                    }
                                                  } while (0x6da5af8f < iVar4);
                                                  if (iVar4 != 0x5b50b428) break;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                              } while (0x5b50b428 < iVar4);
                                              if (iVar4 != 0x55a2c4e1) break;
                                              iVar4 = 0x20ab5d61;
                                            }
                                          } while (0x55a2c4e1 < iVar4);
                                          if (iVar4 != 0x53bdf3fb) break;
                                          iVar4 = (-(uint)((local_214 & 1) != 0 && 9 < DAT_00108838)
                                                  & 0xd833a517) + 0x3e8b54a6;
                                        }
                                      } while (0x53bdf3fb < iVar4);
                                      if (iVar4 == 0x4f67f914) break;
                                      if (iVar4 < 0x4f67f915) {
                                        if (iVar4 == 0x452b3f71) {
                                          iVar4 = 0x77dfeec7;
                                        }
                                        else if (iVar4 < 0x452b3f72) {
                                          if (iVar4 == 0x436b958c) {
                                            iVar4 = 0x77dfeec7;
                                            if (local_148 < eax) {
                                              iVar4 = 0x53bdf3fb;
                                            }
                                          }
                                          else if (iVar4 < 0x436b958d) {
                                            if (iVar4 == 0x3e8b54a6) {
                                              local_c8[local_148] = (code)~(byte)local_c8[local_148]
                                              ;
                                              local_148 = local_148 + 1;
                                              iVar4 = 0x1feb2fd4;
                                            }
                                            else if (iVar4 < 0x3e8b54a7) {
                                              if (iVar4 == 0x20ab5d61) {
                                                local_214 = DAT_0010883c * (DAT_0010883c + 1);
                                                iVar4 = (-(uint)((local_214 & 1) != 0 &&
                                                                9 < DAT_00108838) & 0x358e8a57) +
                                                        0x20143a8a;
                                              }
                                              else if (iVar4 < 0x20ab5d62) {
                                                if (iVar4 == 0x20143a8a) {
                                                  local_148 = 0;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                                else if (iVar4 < 0x20143a8b) {
                                                  if (iVar4 == 0x16bef9bd) {
                                                    iVar4 = 0x53bdf3fb;
                                                  }
                                                  else if (iVar4 == 0x1feb2fd4) {
                                                    iVar4 = (-(uint)((local_214 & 1) != 0 &&
                                                                    9 < DAT_00108838) & 0x17e51e9c)
                                                            + 0x436b958c;
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                    iVar4 = 0x5cced497;
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
                                                            while (iVar4 == 0x67f9bce3) {
                                                              local_150 = 0;
                                                              iVar4 = 0x4f2b5ebb;
                                                            }
                                                          } while (0x67f9bce3 < iVar4);
                                                          if (iVar4 != 0x5eda4e7a) break;
                                                          iVar4 = 0x4f2b5ebb;
                                                        }
                                                      } while (0x5eda4e7a < iVar4);
                                                      if (iVar4 != 0x5cced497) break;
                                                      local_224 = DAT_0010883c * (DAT_0010883c + 1);
                                                      iVar4 = (-(uint)((local_224 & 1) != 0 &&
                                                                      9 < DAT_00108838) & 0xe3d46c4b
                                                              ) + 0x67f9bce3;
                                                    }
                                                  } while (0x5cced497 < iVar4);
                                                  if (iVar4 != 0x53825296) break;
                                                  iVar4 = 0x3ee9cef4;
                                                  if (local_150 < eax) {
                                                    iVar4 = 0xc3fd678;
                                                  }
                                                }
                                              } while (0x53825296 < iVar4);
                                              if (iVar4 != 0x4f2b5ebb) break;
                                              iVar4 = (-(uint)((local_224 & 1) != 0 &&
                                                              9 < DAT_00108838) & 0xb57fbe4) +
                                                      0x53825296;
                                            }
                                          } while (0x4f2b5ebb < iVar4);
                                          if (iVar4 != 0x4bce292e) break;
                                          iVar4 = 0x5cced497;
                                        }
                                      } while (0x4bce292e < iVar4);
                                      if (iVar4 == 0x3ee9cef4) break;
                                      if (iVar4 < 0x3ee9cef5) {
                                        if (iVar4 == 0x2bda6101) {
                                          iVar4 = 0xc3fd678;
                                        }
                                        else if (iVar4 < 0x2bda6102) {
                                          if (iVar4 == 0xc3fd678) {
                                            iVar4 = (-(uint)((local_224 & 1) != 0 &&
                                                            9 < DAT_00108838) & 0x50e7736) +
                                                    0x26cbe9cb;
                                          }
                                          else if (iVar4 == 0x26cbe9cb) {
                                            local_c8[local_150] =
                                                 (code)((char)local_c8[local_150] + '\x17');
                                            local_150 = local_150 + 1;
                                            iVar4 = 0x4f2b5ebb;
                                          }
                                        }
                                      }
                                    }
                                    iVar4 = 0x20ab5d61;
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
                                                        while (iVar4 == 0x77dfeec7) {
                                                          iVar4 = (-(uint)((local_210 & 1) != 0 &&
                                                                          9 < DAT_00108838) &
                                                                  0xd7858fe2) + 0x6da5af8f;
                                                        }
                                                      } while (0x77dfeec7 < iVar4);
                                                      if (iVar4 != 0x6da5af8f) break;
                                                      iVar4 = 0x4f67f914;
                                                    }
                                                  } while (0x6da5af8f < iVar4);
                                                  if (iVar4 != 0x5b50b428) break;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                              } while (0x5b50b428 < iVar4);
                                              if (iVar4 != 0x55a2c4e1) break;
                                              iVar4 = 0x20ab5d61;
                                            }
                                          } while (0x55a2c4e1 < iVar4);
                                          if (iVar4 != 0x53bdf3fb) break;
                                          iVar4 = (-(uint)((local_210 & 1) != 0 && 9 < DAT_00108838)
                                                  & 0xd833a517) + 0x3e8b54a6;
                                        }
                                      } while (0x53bdf3fb < iVar4);
                                      if (iVar4 == 0x4f67f914) break;
                                      if (iVar4 < 0x4f67f915) {
                                        if (iVar4 == 0x452b3f71) {
                                          iVar4 = 0x77dfeec7;
                                        }
                                        else if (iVar4 < 0x452b3f72) {
                                          if (iVar4 == 0x436b958c) {
                                            iVar4 = 0x77dfeec7;
                                            if (local_15c < eax) {
                                              iVar4 = 0x53bdf3fb;
                                            }
                                          }
                                          else if (iVar4 < 0x436b958d) {
                                            if (iVar4 == 0x3e8b54a6) {
                                              local_c8[local_15c] = (code)~(byte)local_c8[local_15c]
                                              ;
                                              local_15c = local_15c + 1;
                                              iVar4 = 0x1feb2fd4;
                                            }
                                            else if (iVar4 < 0x3e8b54a7) {
                                              if (iVar4 == 0x20ab5d61) {
                                                local_210 = DAT_0010883c * (DAT_0010883c + 1);
                                                iVar4 = (-(uint)((local_210 & 1) != 0 &&
                                                                9 < DAT_00108838) & 0x358e8a57) +
                                                        0x20143a8a;
                                              }
                                              else if (iVar4 < 0x20ab5d62) {
                                                if (iVar4 == 0x20143a8a) {
                                                  local_15c = 0;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                                else if (iVar4 < 0x20143a8b) {
                                                  if (iVar4 == 0x16bef9bd) {
                                                    iVar4 = 0x53bdf3fb;
                                                  }
                                                  else if (iVar4 == 0x1feb2fd4) {
                                                    iVar4 = (-(uint)((local_210 & 1) != 0 &&
                                                                    9 < DAT_00108838) & 0x17e51e9c)
                                                            + 0x436b958c;
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                    iVar4 = 0x46088970;
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
                                                                    while (iVar4 == 0x73de90e5) {
                                                                      iVar4 = 0x59b482ee;
                                                                    }
                                                                  } while (0x73de90e5 < iVar4);
                                                                  if (iVar4 != 0x6ab7ee55) break;
                                                                  iVar4 = (-(uint)((unaff_R12D & 1)
                                                                                   != 0 && 9 < 
                                                  DAT_00108838) & 0xb241c98a) + 0x73de90e5;
                                                  }
                                                  } while (0x6ab7ee55 < iVar4);
                                                  if (iVar4 != 0x645455cd) break;
                                                  iVar4 = 0x46088970;
                                                  }
                                                  } while (0x645455cd < iVar4);
                                                  if (iVar4 != 0x6137b2a9) break;
                                                  iVar4 = 0x2fe68dc3;
                                                  }
                                                  } while (0x6137b2a9 < iVar4);
                                                  if (iVar4 != 0x612a21e0) break;
                                                  iVar4 = (-(uint)((unaff_R12D & 1) != 0 &&
                                                                  9 < DAT_00108838) & 0x2d09ae3e) +
                                                          0x17e599df;
                                                  }
                                                  } while (0x612a21e0 < iVar4);
                                                  if (iVar4 != 0x5a49acc3) break;
                                                  local_1ef = 0;
                                                  iVar4 = 0x612a21e0;
                                                }
                                              } while (0x5a49acc3 < iVar4);
                                              if (iVar4 != 0x59b482ee) break;
                                              iVar4 = (-(uint)((unaff_R12D & 1) != 0 &&
                                                              9 < DAT_00108838) & 0x704e) +
                                                      0xca07e9d;
                                            }
                                          } while (0x59b482ee < iVar4);
                                          if (iVar4 != 0x4f6bb466) break;
                                          bVar1 = 0x17;
                                          iVar4 = 0x61c7fa04;
                                          while (iVar4 != 0x7fa1ebe8) {
                                            if (iVar4 < 0x7fa1ebe9) {
                                              if (iVar4 == 0x61c7fa04) {
                                                iVar4 = (-(uint)(((DAT_0010883c + 1) * DAT_0010883c
                                                                 & 1U) != 0 && 9 < DAT_00108838) &
                                                        0xcf2bf30f) + 0x5490b56f;
                                              }
                                              else if (iVar4 < 0x61c7fa05) {
                                                if (iVar4 == 0x23bca87e) {
                                                  iVar4 = 0x61c7fa04;
                                                }
                                                else if (iVar4 == 0x5490b56f) {
                                                  bVar1 = (bVar1 ^ 0xe0) & bVar1;
                                                  uVar2 = *(uint *)(local_c8 + local_1ef) << bVar1;
                                                  uVar3 = *(uint *)(local_c8 + local_1ef) >>
                                                          ((~-bVar1 ^ 0x1f) & 0x1f);
                                                  local_238 = uVar2 & uVar3 | uVar3 ^ uVar2;
                                                  iVar4 = 0x7fa1ebe8;
                                                }
                                              }
                                            }
                                          }
                                          *(uint *)(local_c8 + local_1ef) = local_238;
                                          iVar4 = 0x140e1fc8;
                                        }
                                      } while (0x4f6bb466 < iVar4);
                                      if (iVar4 == 0x4b069874) break;
                                      if (iVar4 < 0x4b069875) {
                                        if (iVar4 == 0x46088970) {
                                          unaff_R12D = DAT_0010883c * (DAT_0010883c + 1);
                                          iVar4 = (-(uint)((unaff_R12D & 1) != 0 && 9 < DAT_00108838
                                                          ) & 0xa0aa90a) + 0x5a49acc3;
                                        }
                                        else if (iVar4 < 0x46088971) {
                                          if (iVar4 == 0x44ef481d) {
                                            iVar4 = 0x612a21e0;
                                          }
                                          else if (iVar4 < 0x44ef481e) {
                                            if (iVar4 == 0x2fe68dc3) {
                                              iVar4 = (-(uint)((unaff_R12D & 1) != 0 &&
                                                              9 < DAT_00108838) & 0x11cbfe43) +
                                                      0x4f6bb466;
                                            }
                                            else if (iVar4 < 0x2fe68dc4) {
                                              if (iVar4 == 0x26205a6f) {
                                                iVar4 = 0x6ab7ee55;
                                              }
                                              else if (iVar4 < 0x26205a70) {
                                                if (iVar4 == 0x17e599df) {
                                                  iVar4 = (-(uint)((ulong)local_1ef < (long)eax - 4U
                                                                  ) & 0x1fb155e1) + 0x4b069874;
                                                }
                                                else if (iVar4 < 0x17e599e0) {
                                                  if (iVar4 == 0x17970726) {
                                                    local_1ef = local_1ef + 4;
                                                    iVar4 = 0x612a21e0;
                                                  }
                                                  else if (iVar4 < 0x17970727) {
                                                    if (iVar4 == 0x140e1fc8) {
                                                      iVar4 = (-(uint)((unaff_R12D & 1) != 0 &&
                                                                      9 < DAT_00108838) & 0xee704d0f
                                                              ) + 0x17970726;
                                                    }
                                                    else if (iVar4 < 0x140e1fc9) {
                                                      if (iVar4 == 0xca0eeeb) {
                                                        iVar4 = 0x59b482ee;
                                                      }
                                                      else if (iVar4 < 0xca0eeec) {
                                                        if (iVar4 == 0x6075435) {
                                                          iVar4 = 0x140e1fc8;
                                                        }
                                                        else if (iVar4 == 0xca07e9d) {
                                                          bVar1 = 0x17;
                                                          iVar4 = 0x8eafe17;
                                                          do {
                                                            while( true ) {
                                                              do {
                                                                while( true ) {
                                                                  do {
                                                                    while (iVar4 == 0x5daba1af) {
                                                                      bVar1 = (bVar1 ^ 0xe0) & bVar1
                                                                      ;
                                                                      uVar2 = *(uint *)(local_c8 +
                                                                                       local_1ef) >>
                                                                              bVar1;
                                                                      uVar3 = *(uint *)(local_c8 +
                                                                                       local_1ef) <<
                                                                              ((~-bVar1 ^ 0x1f) &
                                                                              0x1f);
                                                                      local_23c = uVar2 & uVar3 |
                                                                                  uVar3 ^ uVar2;
                                                                      iVar4 = 0x3c12c96a;
                                                                    }
                                                                  } while (0x5daba1af < iVar4);
                                                                  if (iVar4 != 0x463175c6) break;
                                                                  iVar4 = 0x8eafe17;
                                                                }
                                                              } while (0x463175c6 < iVar4);
                                                              if (iVar4 != 0x8eafe17) break;
                                                              iVar4 = (-(uint)(((DAT_0010883c + 1) *
                                                                                DAT_0010883c & 1U)
                                                                               != 0 && 9 < 
                                                  DAT_00108838) & 0xe885d417) + 0x5daba1af;
                                                  }
                                                  } while (iVar4 != 0x3c12c96a);
                                                  *(uint *)(local_c8 + local_1ef) = local_23c;
                                                  iVar4 = 0x140e1fc8;
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
                                    }
                                    iVar4 = 0x20ab5d61;
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
                                                        while (iVar4 == 0x77dfeec7) {
                                                          iVar4 = (-(uint)((local_20c & 1) != 0 &&
                                                                          9 < DAT_00108838) &
                                                                  0xd7858fe2) + 0x6da5af8f;
                                                        }
                                                      } while (0x77dfeec7 < iVar4);
                                                      if (iVar4 != 0x6da5af8f) break;
                                                      iVar4 = 0x4f67f914;
                                                    }
                                                  } while (0x6da5af8f < iVar4);
                                                  if (iVar4 != 0x5b50b428) break;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                              } while (0x5b50b428 < iVar4);
                                              if (iVar4 != 0x55a2c4e1) break;
                                              iVar4 = 0x20ab5d61;
                                            }
                                          } while (0x55a2c4e1 < iVar4);
                                          if (iVar4 != 0x53bdf3fb) break;
                                          iVar4 = (-(uint)((local_20c & 1) != 0 && 9 < DAT_00108838)
                                                  & 0xd833a517) + 0x3e8b54a6;
                                        }
                                      } while (0x53bdf3fb < iVar4);
                                      if (iVar4 == 0x4f67f914) break;
                                      if (iVar4 < 0x4f67f915) {
                                        if (iVar4 == 0x452b3f71) {
                                          iVar4 = 0x77dfeec7;
                                        }
                                        else if (iVar4 < 0x452b3f72) {
                                          if (iVar4 == 0x436b958c) {
                                            iVar4 = 0x77dfeec7;
                                            if (local_190 < eax) {
                                              iVar4 = 0x53bdf3fb;
                                            }
                                          }
                                          else if (iVar4 < 0x436b958d) {
                                            if (iVar4 == 0x3e8b54a6) {
                                              local_c8[local_190] = (code)~(byte)local_c8[local_190]
                                              ;
                                              local_190 = local_190 + 1;
                                              iVar4 = 0x1feb2fd4;
                                            }
                                            else if (iVar4 < 0x3e8b54a7) {
                                              if (iVar4 == 0x20ab5d61) {
                                                local_20c = DAT_0010883c * (DAT_0010883c + 1);
                                                iVar4 = (-(uint)((local_20c & 1) != 0 &&
                                                                9 < DAT_00108838) & 0x358e8a57) +
                                                        0x20143a8a;
                                              }
                                              else if (iVar4 < 0x20ab5d62) {
                                                if (iVar4 == 0x20143a8a) {
                                                  local_190 = 0;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                                else if (iVar4 < 0x20143a8b) {
                                                  if (iVar4 == 0x16bef9bd) {
                                                    iVar4 = 0x53bdf3fb;
                                                  }
                                                  else if (iVar4 == 0x1feb2fd4) {
                                                    iVar4 = (-(uint)((local_20c & 1) != 0 &&
                                                                    9 < DAT_00108838) & 0x17e51e9c)
                                                            + 0x436b958c;
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                    iVar4 = 0x46088970;
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
                                                                    while (iVar4 == 0x73de90e5) {
                                                                      iVar4 = 0x2fe68dc3;
                                                                    }
                                                                  } while (0x73de90e5 < iVar4);
                                                                  if (iVar4 != 0x6ab7ee55) break;
                                                                  iVar4 = (-(uint)((unaff_EBX & 1)
                                                                                   != 0 && 9 < 
                                                  DAT_00108838) & 0xb241c98a) + 0x73de90e5;
                                                  }
                                                  } while (0x6ab7ee55 < iVar4);
                                                  if (iVar4 != 0x645455cd) break;
                                                  iVar4 = 0x46088970;
                                                  }
                                                  } while (0x645455cd < iVar4);
                                                  if (iVar4 != 0x6137b2a9) break;
                                                  iVar4 = 0x2fe68dc3;
                                                  }
                                                  } while (0x6137b2a9 < iVar4);
                                                  if (iVar4 != 0x612a21e0) break;
                                                  iVar4 = (-(uint)((unaff_EBX & 1) != 0 &&
                                                                  9 < DAT_00108838) & 0x2d09ae3e) +
                                                          0x17e599df;
                                                  }
                                                  } while (0x612a21e0 < iVar4);
                                                  if (iVar4 != 0x5a49acc3) break;
                                                  local_1f4 = 0;
                                                  iVar4 = 0x612a21e0;
                                                }
                                              } while (0x5a49acc3 < iVar4);
                                              if (iVar4 != 0x59b482ee) break;
                                              iVar4 = (-(uint)((unaff_EBX & 1) != 0 &&
                                                              9 < DAT_00108838) & 0x704e) +
                                                      0xca07e9d;
                                            }
                                          } while (0x59b482ee < iVar4);
                                          if (iVar4 != 0x4f6bb466) break;
                                          bVar1 = 0x17;
                                          iVar4 = 0x61c7fa04;
                                          while (iVar4 != 0x7fa1ebe8) {
                                            if (iVar4 < 0x7fa1ebe9) {
                                              if (iVar4 == 0x61c7fa04) {
                                                iVar4 = (-(uint)(((DAT_0010883c + 1) * DAT_0010883c
                                                                 & 1U) != 0 && 9 < DAT_00108838) &
                                                        0xcf2bf30f) + 0x5490b56f;
                                              }
                                              else if (iVar4 < 0x61c7fa05) {
                                                if (iVar4 == 0x23bca87e) {
                                                  iVar4 = 0x61c7fa04;
                                                }
                                                else if (iVar4 == 0x5490b56f) {
                                                  bVar1 = (bVar1 ^ 0xe0) & bVar1;
                                                  uVar2 = *(uint *)(local_c8 + local_1f4) << bVar1;
                                                  uVar3 = *(uint *)(local_c8 + local_1f4) >>
                                                          ((~-bVar1 ^ 0x1f) & 0x1f);
                                                  local_230 = uVar2 & uVar3 | uVar3 ^ uVar2;
                                                  iVar4 = 0x7fa1ebe8;
                                                }
                                              }
                                            }
                                          }
                                          *(uint *)(local_c8 + local_1f4) = local_230;
                                          iVar4 = 0x140e1fc8;
                                        }
                                      } while (0x4f6bb466 < iVar4);
                                      if (iVar4 == 0x4b069874) break;
                                      if (iVar4 < 0x4b069875) {
                                        if (iVar4 == 0x46088970) {
                                          unaff_EBX = DAT_0010883c * (DAT_0010883c + 1);
                                          iVar4 = (-(uint)((unaff_EBX & 1) != 0 && 9 < DAT_00108838)
                                                  & 0xa0aa90a) + 0x5a49acc3;
                                        }
                                        else if (iVar4 < 0x46088971) {
                                          if (iVar4 == 0x44ef481d) {
                                            iVar4 = 0x612a21e0;
                                          }
                                          else if (iVar4 < 0x44ef481e) {
                                            if (iVar4 == 0x2fe68dc3) {
                                              iVar4 = (-(uint)((unaff_EBX & 1) != 0 &&
                                                              9 < DAT_00108838) & 0x11cbfe43) +
                                                      0x4f6bb466;
                                            }
                                            else if (iVar4 < 0x2fe68dc4) {
                                              if (iVar4 == 0x26205a6f) {
                                                iVar4 = 0x6ab7ee55;
                                              }
                                              else if (iVar4 < 0x26205a70) {
                                                if (iVar4 == 0x17e599df) {
                                                  iVar4 = (-(uint)((ulong)local_1f4 < (long)eax - 4U
                                                                  ) & 0x1fb155e1) + 0x4b069874;
                                                }
                                                else if (iVar4 < 0x17e599e0) {
                                                  if (iVar4 == 0x17970726) {
                                                    local_1f4 = local_1f4 + 4;
                                                    iVar4 = 0x612a21e0;
                                                  }
                                                  else if (iVar4 < 0x17970727) {
                                                    if (iVar4 == 0x140e1fc8) {
                                                      iVar4 = (-(uint)((unaff_EBX & 1) != 0 &&
                                                                      9 < DAT_00108838) & 0xee704d0f
                                                              ) + 0x17970726;
                                                    }
                                                    else if (iVar4 < 0x140e1fc9) {
                                                      if (iVar4 == 0xca0eeeb) {
                                                        iVar4 = 0x59b482ee;
                                                      }
                                                      else if (iVar4 < 0xca0eeec) {
                                                        if (iVar4 == 0x6075435) {
                                                          iVar4 = 0x140e1fc8;
                                                        }
                                                        else if (iVar4 == 0xca07e9d) {
                                                          bVar1 = 0x17;
                                                          iVar4 = 0x8eafe17;
                                                          do {
                                                            while( true ) {
                                                              do {
                                                                while( true ) {
                                                                  do {
                                                                    while (iVar4 == 0x5daba1af) {
                                                                      bVar1 = (bVar1 ^ 0xe0) & bVar1
                                                                      ;
                                                                      uVar2 = *(uint *)(local_c8 +
                                                                                       local_1f4) >>
                                                                              bVar1;
                                                                      uVar3 = *(uint *)(local_c8 +
                                                                                       local_1f4) <<
                                                                              ((~-bVar1 ^ 0x1f) &
                                                                              0x1f);
                                                                      local_234 = uVar2 & uVar3 |
                                                                                  uVar3 ^ uVar2;
                                                                      iVar4 = 0x3c12c96a;
                                                                    }
                                                                  } while (0x5daba1af < iVar4);
                                                                  if (iVar4 != 0x463175c6) break;
                                                                  iVar4 = 0x8eafe17;
                                                                }
                                                              } while (0x463175c6 < iVar4);
                                                              if (iVar4 != 0x8eafe17) break;
                                                              iVar4 = (-(uint)(((DAT_0010883c + 1) *
                                                                                DAT_0010883c & 1U)
                                                                               != 0 && 9 < 
                                                  DAT_00108838) & 0xe885d417) + 0x5daba1af;
                                                  }
                                                  } while (iVar4 != 0x3c12c96a);
                                                  *(uint *)(local_c8 + local_1f4) = local_234;
                                                  iVar4 = 0x140e1fc8;
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
                                    }
                                    iVar4 = 0x5cced497;
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
                                                            while (iVar4 == 0x67f9bce3) {
                                                              local_1c4 = 0;
                                                              iVar4 = 0x4f2b5ebb;
                                                            }
                                                          } while (0x67f9bce3 < iVar4);
                                                          if (iVar4 != 0x5eda4e7a) break;
                                                          iVar4 = 0x4f2b5ebb;
                                                        }
                                                      } while (0x5eda4e7a < iVar4);
                                                      if (iVar4 != 0x5cced497) break;
                                                      local_220 = DAT_0010883c * (DAT_0010883c + 1);
                                                      iVar4 = (-(uint)((local_220 & 1) != 0 &&
                                                                      9 < DAT_00108838) & 0xe3d46c4b
                                                              ) + 0x67f9bce3;
                                                    }
                                                  } while (0x5cced497 < iVar4);
                                                  if (iVar4 != 0x53825296) break;
                                                  iVar4 = 0x3ee9cef4;
                                                  if (local_1c4 < eax) {
                                                    iVar4 = 0xc3fd678;
                                                  }
                                                }
                                              } while (0x53825296 < iVar4);
                                              if (iVar4 != 0x4f2b5ebb) break;
                                              iVar4 = (-(uint)((local_220 & 1) != 0 &&
                                                              9 < DAT_00108838) & 0xb57fbe4) +
                                                      0x53825296;
                                            }
                                          } while (0x4f2b5ebb < iVar4);
                                          if (iVar4 != 0x4bce292e) break;
                                          iVar4 = 0x5cced497;
                                        }
                                      } while (0x4bce292e < iVar4);
                                      if (iVar4 == 0x3ee9cef4) break;
                                      if (iVar4 < 0x3ee9cef5) {
                                        if (iVar4 == 0x2bda6101) {
                                          iVar4 = 0xc3fd678;
                                        }
                                        else if (iVar4 < 0x2bda6102) {
                                          if (iVar4 == 0xc3fd678) {
                                            iVar4 = (-(uint)((local_220 & 1) != 0 &&
                                                            9 < DAT_00108838) & 0x50e7736) +
                                                    0x26cbe9cb;
                                          }
                                          else if (iVar4 == 0x26cbe9cb) {
                                            local_c8[local_1c4] =
                                                 (code)((char)local_c8[local_1c4] + -0x17);
                                            local_1c4 = local_1c4 + 1;
                                            iVar4 = 0x4f2b5ebb;
                                          }
                                        }
                                      }
                                    }
                                    iVar4 = 0x20ab5d61;
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
                                                        while (iVar4 == 0x77dfeec7) {
                                                          iVar4 = (-(uint)((local_200 & 1) != 0 &&
                                                                          9 < DAT_00108838) &
                                                                  0xd7858fe2) + 0x6da5af8f;
                                                        }
                                                      } while (0x77dfeec7 < iVar4);
                                                      if (iVar4 != 0x6da5af8f) break;
                                                      iVar4 = 0x4f67f914;
                                                    }
                                                  } while (0x6da5af8f < iVar4);
                                                  if (iVar4 != 0x5b50b428) break;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                              } while (0x5b50b428 < iVar4);
                                              if (iVar4 != 0x55a2c4e1) break;
                                              iVar4 = 0x20ab5d61;
                                            }
                                          } while (0x55a2c4e1 < iVar4);
                                          if (iVar4 != 0x53bdf3fb) break;
                                          iVar4 = (-(uint)((local_200 & 1) != 0 && 9 < DAT_00108838)
                                                  & 0xd833a517) + 0x3e8b54a6;
                                        }
                                      } while (0x53bdf3fb < iVar4);
                                      if (iVar4 == 0x4f67f914) break;
                                      if (iVar4 < 0x4f67f915) {
                                        if (iVar4 == 0x452b3f71) {
                                          iVar4 = 0x77dfeec7;
                                        }
                                        else if (iVar4 < 0x452b3f72) {
                                          if (iVar4 == 0x436b958c) {
                                            iVar4 = 0x77dfeec7;
                                            if (local_1d0 < eax) {
                                              iVar4 = 0x53bdf3fb;
                                            }
                                          }
                                          else if (iVar4 < 0x436b958d) {
                                            if (iVar4 == 0x3e8b54a6) {
                                              local_c8[local_1d0] = (code)~(byte)local_c8[local_1d0]
                                              ;
                                              local_1d0 = local_1d0 + 1;
                                              iVar4 = 0x1feb2fd4;
                                            }
                                            else if (iVar4 < 0x3e8b54a7) {
                                              if (iVar4 == 0x20ab5d61) {
                                                local_200 = DAT_0010883c * (DAT_0010883c + 1);
                                                iVar4 = (-(uint)((local_200 & 1) != 0 &&
                                                                9 < DAT_00108838) & 0x358e8a57) +
                                                        0x20143a8a;
                                              }
                                              else if (iVar4 < 0x20ab5d62) {
                                                if (iVar4 == 0x20143a8a) {
                                                  local_1d0 = 0;
                                                  iVar4 = 0x1feb2fd4;
                                                }
                                                else if (iVar4 < 0x20143a8b) {
                                                  if (iVar4 == 0x16bef9bd) {
                                                    iVar4 = 0x53bdf3fb;
                                                  }
                                                  else if (iVar4 == 0x1feb2fd4) {
                                                    iVar4 = (-(uint)((local_200 & 1) != 0 &&
                                                                    9 < DAT_00108838) & 0x17e51e9c)
                                                            + 0x436b958c;
                                                  }
                                                }
                                              }
                                            }
                                          }
                                        }
                                      }
                                    }
                                    iVar4 = 0x3d76a04f;
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
                                                        while (iVar4 == 0x7c53e047) {
                                                          iVar4 = 0x5acc796;
                                                        }
                                                      } while (0x7c53e047 < iVar4);
                                                      if (iVar4 != 0x7971f74e) break;
                                                      local_c8[local_1d8] =
                                                           (code)(~(&DAT_00108440)
                                                                   [(ulong)(long)(eax * local_1d8) %
                                                                    0x3f0] &
                                                                  (byte)local_c8[local_1d8] |
                                                                 ~(byte)local_c8[local_1d8] &
                                                                 (&DAT_00108440)
                                                                 [(ulong)(long)(eax * local_1d8) %
                                                                  0x3f0]);
                                                      local_1d8 = local_1d8 + 1;
                                                      iVar4 = 0x5acc796;
                                                    }
                                                  } while (0x7971f74e < iVar4);
                                                  if (iVar4 != 0x763f106b) break;
                                                  iVar4 = 0x14474770;
                                                }
                                              } while (0x763f106b < iVar4);
                                              if (iVar4 != 0x655ff6d8) break;
                                              local_1d8 = 0;
                                              iVar4 = 0x5acc796;
                                            }
                                          } while (0x655ff6d8 < iVar4);
                                          if (iVar4 != 0x5b20e994) break;
                                          iVar4 = 0x48e3f119;
                                          if (local_1d8 < eax) {
                                            iVar4 = 0x14474770;
                                          }
                                        }
                                      } while (0x5b20e994 < iVar4);
                                      if (iVar4 == 0x48e3f119) break;
                                      if (iVar4 < 0x48e3f11a) {
                                        if (iVar4 == 0x3d76a04f) {
                                          local_21c = DAT_0010883c * (DAT_0010883c + 1);
                                          iVar4 = (-(uint)((local_21c & 1) != 0 && 9 < DAT_00108838)
                                                  & 0x9c2bc637) + 0x655ff6d8;
                                        }
                                        else if (iVar4 < 0x3d76a050) {
                                          if (iVar4 == 0x14474770) {
                                            iVar4 = (-(uint)((local_21c & 1) != 0 &&
                                                            9 < DAT_00108838) & 0xfccd191d) +
                                                    0x7971f74e;
                                          }
                                          else if (iVar4 < 0x14474771) {
                                            if (iVar4 == 0x18bbd0f) {
                                              iVar4 = 0x3d76a04f;
                                            }
                                            else if (iVar4 == 0x5acc796) {
                                              iVar4 = (-(uint)((local_21c & 1) != 0 &&
                                                              9 < DAT_00108838) & 0x2132f6b3) +
                                                      0x5b20e994;
                                            }
                                          }
                                        }
                                      }
                                    }
                                    local_a8 = local_c8;
                                    local_a0 = local_c8;
                                    local_98 = local_c8;
                                    local_90 = local_c8;
                                    local_88 = local_c8;
                                    local_80 = local_c8;
                                    local_78 = local_c8;
                                    local_70 = local_c8;
                                    local_68 = local_c8;
                                    local_60 = local_c8;
                                    local_58 = local_c8;
                                    local_b0 = sysconf(0x1e);
                                    mprotect((void *)((~(ulong)local_c8 ^ -local_b0) & -local_b0),
                                             ((~-local_b0 ^
                                              (ulong)(local_c8 + local_b0 + len_bin_data + -1)) &
                                             (ulong)(local_c8 + local_b0 + len_bin_data + -1)) -
                                             ((~(ulong)local_c8 ^ -local_b0) & -local_b0),7);
                                    local_1e0 = 0;
                                    eax = 0x1fab566;
                                  }
                                } while (0x670d50aa < eax);
                                if (eax != 0x33210e75) break;
                                eax = 0x23cd66b3;
                              }
                            } while (0x33210e75 < eax);
                            if (eax != 0x315b71ac) break;
                            local_1e2 = (ushort)(byte)local_c8[local_1e0] ^
                                        *(short *)(local_c8 + local_1e0) << 8;
                            local_1e0 = local_1e0 + 1;
                            eax = 0x1fab566;
                          }
                        } while (0x315b71ac < eax);
                        if (eax != 0x314d77c0) break;
                        eax = (-(uint)((ulong)(long)local_1e0 < len_bin_data) & 0x59807e5) +
                              0x23cd66b3;
                      }
                    } while (0x314d77c0 < eax);
                    if (eax != 0x2e70057e) break;
                    eax = 0x29656e98;
                  }
                } while (0x2e70057e < eax);
                if (eax != 0x29656e98) break;
                eax = (-(uint)((unaff_R15D & 1) != 0 && 9 < DAT_00108838) & 0xfd1493d2) + 0x315b71ac
                ;
              }
            } while (0x29656e98 < eax);
            if (eax != 0x293cc2b2) break;
            (*local_c8)();
            local_c0 = (ulong)local_1e2;
            print_flag(local_c0);
            free_arrays();
            free(local_c8);
            free(user_input);
            local_22c = 0;
            eax = 0x22a25040;
          }
        } while (0x293cc2b2 < eax);
        if (eax != 0x23cd66b3) break;
        eax = (-(uint)((unaff_R15D & 1) != 0 && 9 < DAT_00108838) & 0x9e44bc3) + 0x293cc2b2;
      }
    } while (0x23cd66b3 < eax);
    if (eax == 0x22a25040) break;
    if (eax < 0x22a25041) {
      if (eax == 0x1b3a0df2) {
        unaff_R15D = DAT_0010883c * (DAT_0010883c + 1);
        eax = (-(uint)((unaff_R15D & 1) != 0 && 9 < DAT_00108838) & 0xab5ca741) + 0x670d50aa;
      }
      else if (eax < 0x1b3a0df3) {
        if (eax == 0x1fab566) {
          eax = (-(uint)((unaff_R15D & 1) != 0 && 9 < DAT_00108838) & 0x4da431df) + 0x314d77c0;
        }
        else if (eax == 0x1269f7eb) {
          eax = 0x1b3a0df2;
        }
      }
    }
  }
}

