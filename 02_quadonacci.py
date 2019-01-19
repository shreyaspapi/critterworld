import os
from helper import *

fnum = str(input("Enter filenum: "))
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'02'),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'02'),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')

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

t = int(input("Test cases: "))
fin.write(str(t)+'\n')
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
  print(res)
