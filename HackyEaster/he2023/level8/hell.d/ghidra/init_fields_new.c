#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

extern char *DAT_00108840;
extern char *DAT_00108020;

void init_fields(void) {
  int iVar1;
  int local_1c;

  DAT_00108840 = malloc(0x100);
  local_1c = 0;
  while (local_1c < 0x40) {
    DAT_00108840[DAT_00108020[local_1c]] = (char)local_1c;
    local_1c = local_1c + 1;
  }
  return;
}
