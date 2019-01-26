import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '' # Change according to problem number in contest

def first_last(all_plates):
  first = []
  last = []
  for name in all_plates:
    first.append(name[0])
    last.append(name[-1])
  return (first, last)

# Solution
def solution(listOfPlates):
  first, last = first_last(listOfPlates)
  ans = [first[0], last[0]]
  first, last = first[1:], last[1:]
  for i in range(len(first)):
    if ans[-1] in first:
      index = first.index(ans[-1])
      ans.append(first[index])
      ans.append(last[index])
      first[index], last[index] = "", ""
    elif ans[0] in last:
      index = last.index(ans[0])
      ans.insert(0, last[index])
      ans.insert(0, first[index])
      first[index], last[index] = "", ""
  for i in first:
    if i != "":
      return -1
  return ans

# # Sample cases
# SAMPLE = []


# # Build tests
# fnum = input("Enter testfile num: ")
# fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
# fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')
# t = int(input("Test cases: "))
# fin.write(str(t)+'\n')

# TIME = []
# for i in range(t):
#   # Inputs
#   # Result
#   START = datetime.datetime.now()
#   res = solution()
#   END = datetime.datetime.now()
#   TIME.append(START-END)
#   # File write
#   input_line = ''
#   output_line = ''
#   if i+1<t:
#     input_line += '\n'
#     output_line += '\n'
#   fin.write(input_line)
#   fout.write(output_line)
# print("Time:",sum(TIME,datetime.timedelta(0)))