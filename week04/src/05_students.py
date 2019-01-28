'''
## Problem Statement ##
In an exam, some questions are to place certain options in order. For example, in History, battles may be asked to place in chronological order. However, if the students are off by even one in their answers, they receive 0 points! For example, if a-c-b and the student submits c-b-a or c-a-b, he will receive 0!
Surely there must be a better way! If the number of correct pairs are counted, the student will score more but the total marks would increase to [n * (n-1) / 2]. How about checking the maximum number of correct pairings? For example, in the submission above, the student would receive 2 in both cases! This seems nice.
Given the correct order of options as a string, calculate the score of n students for each of their submissions.
Inspired from [CodeChef](https://www.codechef.com/CD112013/problems/CODE06)

## Input Format ##
First line: t test cases
For next 2t lines:
solution n
submissions * n separated by a single space

## Constraints ##
1 ≤ t ≤ 10^4
1 ≤ n ≤ 10^5
1 ≤ |solution| = |submission| ≤ 25

## Output Format ##
A single line per test case containing n scores separated by a single space
'''
import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '05' # Change according to problem number in contest

def position_finder(first, second, array): 
  if array.index(first) < array.index(second): return True
  return False

# Solution
def grade(submitted_answers, correct_answer):
  grades = []
  for submitted_answer in submitted_answers:
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
      grades.append(max(ans))
  return grades

# Sample cases
# print()
# SAMPLE = [
#   ['Blockade of Naboo', 'Battle of Geonosis', 'Battle of Yavin', 'Battle of Hoth', 'Battle of Endor'],
#   ['Battle of Geonosis', 'Battle of Yavin', 'Battle of Hoth', 'Blockade of Naboo', 'Battle of Endor'],
#   ['Battle of Endor', 'Battle of Hoth', 'Battle of Yavin', 'Battle of Geonosis', 'Blockade of Naboo'],
# ]
# print('Sample output:')
# for sample in SAMPLE[1:]:
#   print(grade(sample,SAMPLE[0]))
# print()

# Build tests
fnum = input("Enter testfile num: ")
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')
t = int(input("Test cases: "))
fin.write(str(t)+'\n')

TIME = []
for i in range(t):
  # Inputs
  length = helper.get_random(1,8,25)
  n = helper.get_random(1,1,100)
  solution = ''.join([chr(96+x) for x in list(helper.get_random(length,1,26))])
  submissions = []
  for _ in range(n): submissions.append(helper.shuffle_string(solution))
  print(solution,submissions,length,n)
  # Result
  START = datetime.datetime.now()
  res = grade(submissions,solution)
  END = datetime.datetime.now()
  TIME.append(END-START)
  # File write
  print(i, res,len(res))
  input_line = solution + ' ' + str(n) + '\n' + ' '.join(sub for sub in submissions)
  output_line = ' '.join(str(x) for x in res)
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))