import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '02' # Change according to problem number in contest

def subStrings(string):
  allSubStrings = []
  for i in range(len(string)):
    for j in range(i, len(string)):
      allSubStrings.append(string[i:j+1])
  return allSubStrings

# Solution
def solution(string, start, end):
  return len(set(subStrings(string[start:end+1])))


# Sample cases
SAMPLE = []


# Build tests
fnum = input("Enter testfile num: ")
t = int(input("Test cases: "))
TIME = []
for i in range(t):
  # Inputs
  # Result
  START = datetime.datetime.now()
  res = solution()
  END = datetime.datetime.now()
  TIME.append(START-END)
  # File write
  input_line = ''
  output_line = ''
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
  fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME))