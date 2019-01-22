# 03_bennett
import os
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT

# Solution
def isBennettPair(n,k):
  f = (helper.fact(n)) % (10**k)
  while f>0:
    if f%10 == 0: f/=10
    else: return 'Y'
  return 'N'
  
fnum = str(input("Enter filenum: "))
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'03'),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'03'),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')

t = int(input("Test cases: "))
fin.write(str(t)+'\n')

# Build test cases
START = datetime.datetime.now()
for i in range(t):
  n = helper.getRandom(1,1,100)
  k = helper.getRandom(1,1,helper.numDigits(helper.fact(n)))
  res = isBennettPair(n,k)
  line = str(n) + ' ' +  str(k)
  out = str(res)
  if i+1<t:
    line += '\n'
    out += '\n'
  fin.write(line)
  fout.write(out)
print(datetime.datetime.now()-START)