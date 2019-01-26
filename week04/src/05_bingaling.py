import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '' # Change according to problem number in contest

def firstLast(allPlates):
  first = []
  last = []
  for name in allPlates:
    first.append(name[0])
    last.append(name[-1])
  return (first, last)

# Solution
def solution(listOfPlates):
  first, last = firstLast(listOfPlates)
  flag = 0
  for i in range(len(first)):
    temp = 0
    for j in range(len(last)):
      if last[i] == first[j]:
          first[j] == ""
          temp = 1
          break
    if temp == 0:
      flag += 1
  if flag < 2:
    return "Y"
  return "N"

# Sample cases
SAMPLE = []


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