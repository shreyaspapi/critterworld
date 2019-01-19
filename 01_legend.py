# 01_legend-has-it
import os
from helper import *

# Calculate Height function
def calc_ht(h,c,n):
  for i in range(c,n+c):
    if isPrime(i): continue
    if i%2==0: h*=4
    h+=20*i
  return h

# sample testcase
print(calc_ht(10,1,10))
print(calc_ht(666,69,234))
print(calc_ht(498,20,400))

fnum = str(input("Enter filenum: "))
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'01'),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'01'),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')

t = int(input("Test cases: "))
fin.write(str(t)+'\n')

# Build test cases
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