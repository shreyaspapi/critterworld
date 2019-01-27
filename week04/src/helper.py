import os
import sys
import random

WEEK_NUM = '04' # Change accordingly
WEEK_PRE = 'week'
HERE = os.path.join(WEEK_PRE+WEEK_NUM,'src')

WORDS = []
with open(os.path.join(HERE,'dictionary.txt')) as dict_file:
  for line in dict_file.readlines(): WORDS.append(line[:-1]) # Remove '\n'
print(WORDS)

# dir struct
TEST_DIR = os.path.join(HERE,'tests')
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
def get_random(n,start,end):
  if n == 1: return random.randint(start,end)
  res = ()
  for _ in range(n): res += (random.randint(start,end),)
  return res

def shuffle_list(lst):
  # shuffle replaces *in place*, use sample instead
  return random.sample(lst, len(lst))