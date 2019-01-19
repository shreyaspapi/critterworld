# dir struct

TEST_DIR = 'tests'
FILE_EXT = '.txt'

INPUT_DIR = 'input'
INPUT_PRE = 'input'

OUTPUT_DIR = 'output'
OUTPUT_PRE = 'output'

# functions
def getRandom(n,start,end):
  res = ()
  import random
  for i in range(n): res += (random.randint(start,end),)
  print(res)
  return res
