import datetime
import sys
# sys.setrecursionlimit(2999)

# dir struct

TEST_DIR = 'tests'
FILE_EXT = '.txt'

INPUT_DIR = 'input'
INPUT_PRE = 'input'

OUTPUT_DIR = 'output'
OUTPUT_PRE = 'output'

# functions
def getRandom(n,start,end):
  import random
  if n == 1: return random.randint(start,end)
  res = ()
  for _ in range(n): res += (random.randint(start,end),)
  return res

def gcd(a,b):
  if b==0: return a
  return gcd(b,a%b)

def xgcd(a,b):
  prevx,x = 1,0
  prevy,y = 0,1
  while b:
    q = a//b
    x,prevx = prevx-q*x,x
    y,prevy = prevy-q*y,y
    a,b = b,a%b
  return a,prevx,prevy

def isPrime(n):
  for i in range(2,n):
    if n%i==0: return False
  if n>1: return True
  else: return False

def numDigits(n,count=0):
  if n>0: return numDigits(n//10,count+1)
  return count

def fact(n,p=1):
  if n==1: return p
  return fact(n-1,p*n)

def getRandomPrime(n,start,end):
  res = ()
  for _ in range(n):
    t = getRandom(1,start,end)
    while not isPrime(t) and t not in res: t = getRandom(1,start,end)
    if n==1: return t
    res += (t,)
  return res
