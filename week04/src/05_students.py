'''
## Problem Statement ##

## Input Format ##

## Constraints ##

## Output Format ##
'''
import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '' # Change according to problem number in contest

def position_finder(first, second, array): 
  if array.index(first) < array.index(second): return True
  return False


# Solution
def grade(submitted_answer, correct_answer):
  length = len(submitted_answer)
  ans = []
  for i in range(length):
    flag = 0
    current = submitted_answer[i]
    for j in range(i+1, length):
      if position_finder(current, submitted_answer[j], correct_answer):
        flag += 1
        current = submitted_answer[j]
    ans.append(flag)
  return max(ans)

# Sample cases
print()
SAMPLE = [
  ['Blockade of Naboo', 'Battle of Geonosis', 'Battle of Yavin', 'Battle of Hoth', 'Battle of Endor'],
  ['Battle of Geonosis', 'Battle of Yavin', 'Battle of Hoth', 'Blockade of Naboo', 'Battle of Endor'],
  ['Battle of Endor', 'Battle of Hoth', 'Battle of Yavin', 'Battle of Geonosis', 'Blockade of Naboo'],
]
print('Sample output:')
for sample in SAMPLE[1:]:
  print(grade(sample,SAMPLE[0]))
print()

# Build tests
fnum = input("Enter testfile num: ")
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')
t = int(input("Test cases: "))
fin.write(str(t)+'\n')

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
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))