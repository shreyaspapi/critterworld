# 04_RsArSaRsA00
import os
from helper import *

# Sample test case
# 7 11 13 -> 37 
# 61 53 17 -> 2753

fnum = str(input("Enter filenum: "))
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'04'),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'04'),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')

t = int(input("Test cases: "))
fin.write(str(t)+'\n')

# Build test cases
START = datetime.datetime.now()
for i in range(t):
  # generate prime p and q
  # choose e
  # calculate d
  res = calc_private(p,q,e)
  line = str(p) + ' ' +  str(q) + ' ' + str(e)
  out = str(res)
  if i+1<t:
    line += '\n'
    out += '\n'
  fin.write(line)
  fout.write(out)
print(datetime.datetime.now()-START)