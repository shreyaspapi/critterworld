# 02_quadonacci
import os
from helper import *

# Quadonacci generator (recursion depth: 1000)
def quad(a,b,c,d,n):
  if n==4: return d
  if n==3: return c
  if n==2: return b
  if n==1: return a
  if n<1: return -1
  e = a+b+c+d
  f = e+b+c+d
  g = e+f+c+d
  h = e+f+g+d
  return quad(e,f,g,h,n-4)

# Sample test case
print(quad(1,1,1,1,9))
print(quad(2,4,6,10,10))
print(quad(53,59,67,71,2100))

fnum = str(input("Enter filenum: "))
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'02'),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'02'),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')

t = int(input("Test cases: "))
fin.write(str(t)+'\n')

# Build test cases
START = datetime.datetime.now()
for i in range(t):
  a,b,c,d,n = getRandom(5,1,1000)
  res = quad(a,b,c,d,n)
  line = str(a) + ' ' +  str(b) + ' ' + str(c) + ' ' + str(d) + ' ' + str(n)
  out = str(res)
  if i+1<t:
    line += '\n'
    out += '\n'
  fin.write(line)
  fout.write(out)
print(datetime.datetime.now()-START)