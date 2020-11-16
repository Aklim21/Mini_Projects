#! python3

import sys

print('Hey you printed to cmd!')

args = sys.argv

for i in args:
    i = int(i)
    if i < 5:
        print ('smol\n')
    else:
        print ('BIGGO!\n')
