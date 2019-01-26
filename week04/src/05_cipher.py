import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '' # Change according to problem number in contest

# Solution
def solution():
  pass

# Sample cases
SAMPLE = []


# Build tests
fnum = input("Enter testfile num: ")
t = int(input("Test cases: "))
TIME = []
for i in range(t):
  # Inputs
  n = helper.get_random(1,1,100)
  length = helper.get_random(1,1,n*n)
  underscores = n*n - length
  alphabets = list(helper.get_random(length,1,26))
  string = [chr(64+x) for x in alphabets]
  string += [chr(95)] * underscores
  string = helper.shuffle_list(string)
  message = ''.join(string)
  # Result
  START = datetime.datetime.now()
  res = solution()
  END = datetime.datetime.now()
  TIME.append(START-END)
  # File write
  input_line = str(n) + '\n' + message
  output_line = ''
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
  fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME))