import os
import sys

from pathlib import Path
from shutil import copy2


if len(sys.argv) < 3:
    print('Please provide two arguments:\n first one is text file location\n second one is target directory location')
    sys.exit()

EXCLUDE_DIRECTORY_COUNT = 4
file = sys.argv[1]
target_dir = Path(sys.argv[2])

if not os.path.exists(file):
    sys.exit('Invalid file')

total = 0
with open(file, 'r') as f:
    for line in f:
        if len(line) <= 1:
            print('continue')
            continue
        path = line.strip('\n')
        print("Copying " + path)
        path = Path(path)
        dir = target_dir.joinpath(*path.parts[EXCLUDE_DIRECTORY_COUNT:-1])
        if not os.path.exists(dir):
            os.makedirs(dir)
        copy2(path, dir)
        total += 1
print('copied ' + str(total))