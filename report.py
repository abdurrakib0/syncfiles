import os
import sys

from pathlib import Path
from shutil import copy2

if len(sys.argv) < 3:
    print('Please provide two arguments:\n first one is text file location\n second one is target directory location')
    sys.exit()

EXCLUDE_DIRECTORY_COUNT = 4
target_dir = sys.argv[2]
temp_dir = target_dir.rstrip('/') + '/'

with open(sys.argv[1]) as f:
    for line in f:
        print("Copying " + line)
        path = Path(line)
        dir = temp_dir + '/'.join(path.parts[EXCLUDE_DIRECTORY_COUNT:-1])
        if not os.path.exists(dir):
            os.makedirs(dir)
        copy2(line.strip('\n'), dir)