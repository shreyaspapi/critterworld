import datetime

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
  for i in range(n): res += (random.randint(start,end),)
  return res

def gcd(a,b):
  if b==0: return a
  return gcd(b,a%b)
  
def isPrime(n):
  for i in range(2,n):
    if n%i==0: return False
  if n>1: return True
  else: return False