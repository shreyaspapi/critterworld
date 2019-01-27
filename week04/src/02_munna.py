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
1 ≤ t ≤ 25000
1 ≤ |s| ≤ 100
1 ≤ start ≤ end ≤ |s|

## Output Format ##
For each question, print a single line containing the integer
'''
import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '02' # Change according to problem number in contest

# Solution
def distinct_substrings(string, start, end):
  sub = string[start:end+1]
  subs = []
  for i in range(len(sub)):
    for j in range(i, len(sub)):
      subs.append(sub[i:j+1])
  return len(set(subs))


# Sample cases
print()
SAMPLE = [
  {'string': 'aabb', 'start': 1, 'end': 3},
  {'string': 'aabbcc', 'start': 2, 'end': 5},
  {'string': 'vwznubfitkdexrqqmedtycnfk', 'start': 12, 'end': 17},
  {'string': 'nlovipenxsdekjhpumufpdxqmhppsenky', 'start': 16, 'end': 25},
]
print('Sample Output:')
for sample in SAMPLE:
  print(distinct_substrings(sample['string'],sample['start'],sample['end']))
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
  n = helper.get_random(1,2,100)
  string = ''.join(chr(96+x) for x in helper.get_random(n,1,26))
  start = helper.get_random(1,0,n-1)
  end = helper.get_random(1,start,n-1)
  # Result
  START = datetime.datetime.now()
  res = distinct_substrings(string,start,end)
  END = datetime.datetime.now()
  TIME.append(END-START)
  # File write
  print(i,res)
  input_line = string + '\n' + str(start) + ' ' + str(end)
  output_line = str(res)
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))