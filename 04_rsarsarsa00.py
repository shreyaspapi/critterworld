# 04_RsArSaRsA00
import os
from helper import *

# Solution
def compute_d(phi,e):
  g,x,_ = xgcd(e,phi)
  return x%phi

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
  p,q = getRandomPrime(2,1,10**6)
  phi = (p-1)*(q-1)
  e = getRandomPrime(1,1,min(phi,10**6))
  d = compute_d(phi,e)
  line = str(p) + ' ' +  str(q) + ' ' + str(e)
  out = str(d) + ' ' + str(p*q)
  if i+1<t:
    line += '\n'
    out += '\n'
  fin.write(line)
  fout.write(out)
print(datetime.datetime.now()-START)