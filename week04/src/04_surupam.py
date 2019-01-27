'''
## Problem Statement ##
A group of archaeologists were searching for treasure. Along the way, they faced many obstacles and overcame them all. However just before the last door, they find a stack of tablets with gibberish written on it. One non spaced word in the lowercase english alphabet per tablet.
Heiroglyphics next to it revealed that the way to open the last door was to arrange the tablets so that the first letter of each tablet is the same as the last letter of each tablet. For now, the archaeologists wondered whether such a pattern is even possible. However, archaeologists are not that good in programming and hence have come to you for help.
Given the words inscribed on each tablet, figure out whether such a pattern is possible or not.

## Input Format ##
First line: t test cases
Next 2t lines:
n: number of tablets
words: the words on the tablet separated by a single space

## Constraints ##
1 ≤ t ≤ 5000
1 ≤ n ≤ 1000

## Output Format ##
'Y' or 'N'
'''
import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '04' # Change according to problem number in contest

# Solution
def is_chain(words):
  first, last = helper.first_last(words)
  flag = 0
  for i in range(len(first)):
    start = True
    for j in range(len(last)):
      if i==j: continue # Same word
      if last[i] == first[j]:
        first[j] = ''
        start = False
        break
    if start: flag += 1
    if flag>1: return 'N'
  return 'Y'


# Sample cases
print()
SAMPLE = [
  ['abhajbh','hhbhuc','chbhueb','buhebu','uhcksbjnd','dbjskj'],
  ['asia','america','and','denmark','kangaroo','oat','tango','tao'],
]
print('Sample Output')
for arr in SAMPLE:
  print(is_chain(helper.shuffle_list(arr)))
print()


# Build tests
fnum = input('Enter testfile num: ')
fin = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),INPUT_DIR),INPUT_PRE+fnum+FILE_EXT),'w')
fout = open(os.path.join(os.path.join(os.path.join(TEST_DIR,PROBLEM_NUM),OUTPUT_DIR),OUTPUT_PRE+fnum+FILE_EXT),'w')
t = int(input('Test cases: '))
fin.write(str(t)+'\n')

TIME = []
for i in range(t):
  # Inputs
  n = helper.get_random(1,2,1000)
  words = [helper.WORDS[x] for x in helper.get_unique_random(n,0,127141)]
  # Result
  START = datetime.datetime.now()
  res = is_chain(words)
  END = datetime.datetime.now()
  TIME.append(END-START)
  # File write
  # print(i,res)
  if res=='Y': print(i)
  input_line = str(len(words)) + '\n' + ' '.join(word for word in words)
  output_line = res
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print('Time:',sum(TIME,datetime.timedelta(0)))