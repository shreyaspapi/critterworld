# -*- coding: utf-8 -*-
# 05_rSaRsArSa01
import os
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT

def modpow_list(lst,e,n):
  return [pow(x,e,n) for x in lst]

# Sample cases
SAMPLE = ['MYNAMEIS','WHAT','ATTACKATDAWN']
P,Q,E,D = (7,11,13,37)
for sample in SAMPLE:
  alphabets = [ord(x)-64 for x in sample]
  encrypted = modpow_list(alphabets,E,P*Q)
  decrypted = modpow_list(encrypted,D,P*Q)
  print(len(sample))
  print(''.join(str(x)+' ' for x in encrypted).strip())
  print(''.join(chr(64+x) for x in decrypted))

fnum = str(input("Enter filenum: "))
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'05'),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,'05'),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')

# Build test cases
t = int(input("Test cases: "))
fin.write(str(t)+'\n')
START = datetime.datetime.now()
for i in range(t):
  # make keys
  while True:
    p,q = helper.getRandomPrime(2,1,10**3)
    n = p*q
    phi = (p-1)*(q-1)
    e = helper.getRandomPrime(1,2,min(phi,10**3))
    g,d,_ = helper.xgcd(e,phi)
    d %= phi
    if p!=q and g==1: break
  l = helper.getRandom(1,2,10**2)
  alphabets = list(helper.getRandom(l,1,26))
  encrypted = modpow_list(alph_list,e,n)
  decrypted = modpow_list(enc_list,d,n)
  plaintext = ''.join(chr(64+x) for x in decrypted)
  # File write
  line = str(l) + '\n' + ''.join(str(x)+' ' for x in encrypted).strip() + '\n' + str(p) + ' ' +  str(n) + ' ' + str(e)
  out = plaintext
  if i+1<t:
    line += '\n'
    out += '\n'
  fin.write(line)
  fout.write(out)
print(datetime.datetime.now()-START)