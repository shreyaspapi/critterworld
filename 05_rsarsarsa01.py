# -*- coding: utf-8 -*-
# 05_rSaRsArSa01
import os
from helper import *

def encrypt_list(lst,e,n):
  return [pow(x,e,n) for x in lst]

def decrypt_list(lst,d,n):
  return [pow(x,d,n) for x in lst]

def encrypt(plain,e,n):
  cipher = ''
  for x in plain:
    cipher += chr(pow(ord(x),e,n))
  return cipher

def decrypt(cipher,d,n):
  plain = ''
  for x in cipher:
    plain += chr(pow(ord(x),d,n))
  return plain

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
    p,q = getRandomPrime(2,1,10**3)
    if p!=q: break
  phi = (p-1)*(q-1)
  while True:
    e = getRandomPrime(1,2,min(phi,10**3))
    g,d,_ = xgcd(e,phi)
    d %= phi
    if g==1: break
  n = p*q
  print(g,p,q,e,d,n)
  print(e*d%phi)

  # make plaintext
  l = getRandom(1,2,10**2)
  alph_list = list(getRandom(l,1,26))
  plaintext = ''
  for x in alph_list: plaintext += chr(64+x)

  encrypted = encrypt(plaintext,e,n)
  decrypted = decrypt(encrypted,d,n)

  enc_list = encrypt_list(alph_list,e,n)
  dec_list = decrypt_list(enc_list,d,n)

  dec = ''
  for x in dec_list: dec += chr(64+x)


  if alph_list != dec_list: raise Exception('FALSE NIBBA!')

  line = str(l) + '\n'
  for x in enc_list: line+=str(x)+' '
  line += '\n' + str(p) + ' ' +  str(n) + ' ' + str(e)
  out = plaintext
  if i+1<t:
    line += '\n'
    out += '\n'
  fin.write(line)
  fout.write(out)

#Sample cases
# sample = ['MYNAMEIS','WHAT','ATTACKATDAWN']
# P,Q,E,D = (7,11,13,37)
# for s in sample:
#   lst = [ord(x)-64 for x in s]
#   enc_list = encrypt_list(lst,E,P*Q)
#   dec_list = decrypt_list(enc_list,D,P*Q)
#   dec = ''
#   for x in dec_list: dec+=chr(64+x)
#   print(enc_list)
#   print(dec)

print(datetime.datetime.now()-START)