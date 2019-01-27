'''
## Problem Statement ##
Munna Bhai is up to his antics again. This time his chacha is coming from the village and seeing what Munna is doing. This would be all good except that Munna's chacha thinks that Munna is software programmer. He needs to get a degree fast to prove that he is one. Luckily, he found an institution who after seeing Munna's enthusiasm, the dean offered him an experimental exam format. He would give Munna 6 exams based on the same problem. He needs to just write the answer for the questions in those exams. The number of exams correctly solved will be the number of certifications Munna receives.
The problem was as follows:
Given a string of characters and a start and end index, find the number of distinct substrings in the range, both inclusive. Munna being Munna, he wore his airpods to the exam, hidden under his beanie. He tells you the string over the phone and the start and end index. You need to tell him the answer for every case.
Note
Distinct substrings of 'aabb',1,3 are 'a', 'b', 'ab', 'bb', 'abb'

## Input Format ##
First line: t test cases
Next 2t lines:
String s
start end

## Constraints ##
1 ≤ t ≤ 10^5
1 ≤ |s| ≤ 10^3
1 ≤ start ≤ end ≤ |s|

## Output Format ##
For each question, print a single line containing the integer
'''
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
  TIME.append(END-START)
  # File write
  input_line = ''
  output_line = ''
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))