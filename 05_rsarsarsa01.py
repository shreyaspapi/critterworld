# 05_rSaRsArSa01

import os
from helper import *

fnum = str(input("Enter filenum: "))
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'05'),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'05'),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')

# Build test cases
t = int(input("Test cases: "))
fin.write(str(t)+'\n')
START = datetime.datetime.now()
for i in range(t):
  h,c = getRandom(2,1,10**3)
  n = getRandom(1,1,10**3)
  res = calc_ht(h,c,n)
  line = str(h) + ' ' +  str(c) + ' ' + str(n)
  out = str(res)
  if i+1<t:
    line += '\n'
    out += '\n'
  fin.write(line)
  fout.write(out)
print(datetime.datetime.now()-START)