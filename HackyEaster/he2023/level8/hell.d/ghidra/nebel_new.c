extern *char base64_alphabet;
extern *char DAT_00108020;

void *nebel(char *user_input, ulong user_input_len, size_t *param_3) {
  typedef unsigned int uint;
  int eax;
  uint unaff_EBX;
  uint unaff_R12D;
  uint unaff_R13D;
  uint unaff_R14D;
  uint unaff_R15D;
  void *local_88;
  int local_5c;
  int local_58;
  uint local_54;
  uint local_50;
  uint local_4c;
  int local_48;
  void *decoded_arr;

  if (base64_alphabet == NULL)
    init_fields();
  *param_3 = (user_input_len >> 2) * 3;
  if (user_input[user_input_len - 1] == '=') {
    *param_3 = *param_3 - 1;
  }
  if (user_input[user_input_len - 2] == '=') {
    *param_3 = *param_3 - 1;
  }
  decoded_arr = malloc(*param_3);
  if (decoded_arr == NULL) {
    eax = 0x1decf8fb;
  } else {
    local_5c = 0;
    local_58 = 0;
    eax = 0xdb0c806;
  }

  while (eax != 0x25125661) {

    if (eax == 0xdb0c806) {
      if (local_5c < user_input_len) {
        if (user_input[local_5c] == '=') {
          unaff_R12D = 0;
        } else {
          unaff_R12D = base64_alphabet[user_input[local_5c]];
        }
        eax = 0xf4d38e2;
        local_5c = local_5c + 1;
      } else {
        local_88 = decoded_arr;
        eax = 0x25125661;
      }
    }

    if (eax == 0xf4d38e2) {
      unaff_R13D =base64_alphabet[user_input[local_5c]];
      local_5c = local_5c + 1;

      if (user_input[local_5c] == '=') {
        unaff_R14D = 0;
      } else {
        unaff_R14D =base64_alphabet[user_input[local_5c]];
      }

      local_5c = local_5c + 1;

      if (user_input[local_5c] == '=') {
        unaff_R15D = 0;
      } else {
        unaff_R15D =base64_alphabet[user_input[local_5c]];
      }
      local_5c = local_5c + 1;

      local_48 =
          unaff_R15D + unaff_R12D * 0x40000 + unaff_R13D * 0x1000 + unaff_R14D * 0x40;
      if (local_58 < *param_3) {
        decoded_arr[local_58] = local_48 >> 0x10;
        local_58 = local_58 + 1;
      }
      if (local_58 < *param_3) {
        decoded_arr[local_58] = local_48 >> 8;
        local_58 = local_58 + 1;
      }
      if (local_58 < *param_3) {
        decoded_arr[local_58] = local_48;
        local_58 = local_58 + 1;
      } 
      eax = 0xdb0c806;
    }

    if (eax == 0x1decf8fb) {
      local_88 = (void *)0x0;
      eax = 0x25125661;
    } // malloc failed
  }
  return local_88;
}
