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

print(firstLast(["shbvhjm","pfsuhygyufs","bygvsfytvesg","gujikgbhfsekjbt","phjbsfp"]))

# Solution
def solution(listOfPlates):
  first, last = firstLast(listOfPlates)

  for i in range(len(first)):
    for j in range(len(last)):
      if i != j:
        if last[i] == first[j]:
          first


# # Sample cases
# SAMPLE = []


# # Build tests
# fnum = input("Enter testfile num: ")
# t = int(input("Test cases: "))
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
#   fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
#   fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')
#   fin.write(input_line)
#   fout.write(output_line)
# print("Time:",sum(TIME))
