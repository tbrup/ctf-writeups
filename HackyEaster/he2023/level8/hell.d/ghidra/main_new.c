undefined4 main(void)

{
  byte bVar1;
  int eax;
  uint uVar2;
  uint uVar3;
  int iVar4;
  size_t sVar5;
  undefined4 local_22c;
  ushort local_1e2;
  int local_1e0;
  int i;
  ulong len_bin_data;
  char *user_input;
  char *bin_data;
  ulong local_c0;
  size_t user_input_len;
  long local_b0;
  char *user_input_ptr;

 eax = 0x670d50aa; 
  while (eax != 0x22a25040) {
    if (eax == 0x670d50aa) {
      user_input_len = 0;
      len_bin_data = 0;
      init_stdio();
      setup_signals();
      puts("Welcome to....");
      puts("Entrance free, it\'s just the flag that will cost your sanity!");
      puts("=========================================================== ");
      user_input = (char *)malloc(0x100);
      fgets(user_input, 0x100, stdin);
      sVar5 = strcspn(user_input, "\n");
      user_input[sVar5] = '\0';
      user_input_len = strlen(user_input);
      user_input_ptr = user_input;
      //
      // refactored to a loop
      for (i = 0; i < user_input_len; i++) {
        user_input[i] = user_input[i] + -0xd;
      }

      /* local_50 = user_input; */
      for (i = 0; i < user_input_len; i += 4) {
        bVar1 = 0x15;
        ptr = &(user_input[i])
        uVar2 = *ptr << bVar1;
        uVar3 = *ptr >> ((~-bVar1 ^ 0x1f) & 0x1f);
        *ptr = uVar2 & uVar3 | uVar3 ^ uVar2;
      }

      bin_data = decode_base64_input(user_input, user_input_len,
                                             &len_bin_data);
      eax = (int)len_bin_data;

      for (i = 0; i < (len_bin_data - 4); i += 4) {
        ptr = &(bin_data[i]);
        bVar1 = 7;
        uVar2 = *ptr >> bVar1;
        uVar3 = *ptr << ((~-bVar1 ^ 0x1f) & 0x1f);
        *ptr = uVar2 & uVar3 | uVar3 ^ uVar2;
      }

      for (i = 0; i < len_bin_data; i++) {
        bin_data[i] = ~bin_data[i];
      }
      for (i = 0; i < len_bin_data; i++) {
        bin_data[i] = ~bin_data[i];
      }

      for (i = 0; i < len_bin_data ; i++) {
          bin_data[i] = bin_data[i] + '\x17';
      }
      
      for (i = 0; i < len_bin_data; i++) {
        bin_data[i] = ~bin_data[i];
      }

      for (i = 0; i < (len_bin_data - 4); i += 4) {
        ptr = &(bin_data[i]);
          bVar1 = 0x17;
        uVar2 = *ptr >> bVar1;
        uVar3 = *ptr << ((~-bVar1 ^ 0x1f) & 0x1f);
        *ptr = uVar2 & uVar3 | uVar3 ^ uVar2;
      }

      for (i = 0; i < len_bin_data; i++) {
        bin_data[i] = ~bin_data[i];
      }

      for (i = 0; i < (len_bin_data - 4); i += 4) {
        ptr = &(bin_data[i]);
          bVar1 = 0x17;
        uVar2 = *ptr >> bVar1;
        uVar3 = *ptr << ((~-bVar1 ^ 0x1f) & 0x1f);
        *ptr = uVar2 & uVar3 | uVar3 ^ uVar2;
      }
      
      for (i = 0; i < len_bin_data ; i++) {
          bin_data[i] = bin_data[i] - '\x17';
      }
      
      for (i = 0; i < len_bin_data; i++) {
        bin_data[i] = ~bin_data[i];
      }
      
      for (i = 0; i < len_bin_data; i++) {
            bin_data[i] =
                :while(~(&DAT_00108440)[(len_bin_data * i) % 0x3f0] & bin_data[i] |
                       ~bin_data[i] & (&DAT_00108440)[(len_bin_data * i) % 0x3f0]);
      }
      
      local_b0 = sysconf(0x1e);
      mprotect(
          (void *)((~(ulong)bin_data ^ -local_b0) & -local_b0),
          ((~-local_b0 ^ (ulong)(bin_data + local_b0 + len_bin_data + -1)) &
           (ulong)(bin_data + local_b0 + len_bin_data + -1)) -
              ((~(ulong)bin_data ^ -local_b0) & -local_b0),
          7);
      local_1e0 = 0;
      eax = 0x1fab566;
    }

    if (eax == 0x1fab566) {
      /* eax = (-(uint)((ulong)(long)local_1e0 < len_bin_data) & 0x59807e5) + 0x23cd66b3; */
      if (local_1e0 < len_bin_data) {
            local_1e2 = (ushort)(byte)bin_data[local_1e0] ^
                        *(short *)(bin_data + local_1e0) << 8;
            local_1e0 = local_1e0 + 1;
            eax = 0x1fab566;
      } else {
            (*bin_data)();
            local_c0 = (ulong)local_1e2;
            print_flag(local_c0);
            free_arrays();
            free(bin_data);
            free(user_input);
            local_22c = 0;
            eax = 0x22a25040;
      }
    }
  }
}
