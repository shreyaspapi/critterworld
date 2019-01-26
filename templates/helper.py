import sys

# dir struct

TEST_DIR = 'tests'
FILE_EXT = '.txt'

INPUT_DIR = 'input'
INPUT_PRE = 'input'

OUTPUT_DIR = 'output'
OUTPUT_PRE = 'output'

# functions

''' 
Get n random numbers in range [start,end]
Returns single number (n==1) or a tuple (n>1)
'''
def getRandom(n,start,end):
  import random
  if n == 1: return random.randint(start,end)
  res = ()
  for _ in range(n): res += (random.randint(start,end),)
  return res