'''
## Problem Statement ##
A group of archaeologists were searching for treasure. Along the way, they faced many obstacles and overcame them all. However just before the last door, they find a stack of tablets with gibberish written on it. One non spaced word in the lowercase english alphabet per tablet.
Heiroglyphics next to it revealed that the way to open the last door was to arrange the tablets so that the first letter of each tablet is the same as the last letter of each tablet. Previously, the archaeologists figured out whether such a pattern is possible or not.
Now, they wish to find the patterns for the given tablets and open the door! They have also discovered an additional step in the code generator. The code to open the door must be the first and last letters of the words on the tablet, sorted lexicographically, and only contain unique letters. So, if the pattern generated is abhajbh-hhbhuc-chbhueb-buhebu-uhcksbjnd-dbjskj, the code to open the door would be abcdhju.
However, have come to you for help again. Given the words inscribed on each tablet, figure out whether such a pattern is possible or not. If possible, print the code to open the door. If not, output 0

## Input Format ##
First line: t test cases
Next 2t lines:
n: Number of words
words: Words inscribed on tablets separated by a space

## Constraints ##
1 ≤ t ≤ 50000
1 ≤ n ≤ 100

## Output Format ##
0 or the code
'''
import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '05' # Change according to problem number in contest

# Solution
def make_chain(words):
  first,last = helper.first_last(sorted(words)) # Sorting important as taking from first word below
  ans = [first[0],last[0]]
  first, last = first[1:], last[1:]
  for item in first:
    if ans[-1] in first:
      index = first.index(ans[-1])
      ans.append(first[index])
      ans.append(last[index])
      first[index],last[index] = '',''
    elif ans[0] in last:
      index = last.index(ans[0])
      ans.insert(0, last[index])
      ans.insert(0, first[index])
      first[index],last[index] = '',''
  for i in first:
    if i != '': return '0'
  return ''.join(iter(sorted(list(set(ans)))))


# Sample cases
print()
SAMPLE = [
  ['abhajbh','hhbhuc','chbhueb','buhebu','uhcksbjnd','dbjskj'],
  ['asia','america','denmark','kangaroo','and','tango','oat','rat'],
  ['asia','america','denmark','kangaroo','and','tango','oat','tao','oscar','rat'],
]
print('Sample Output')
for arr in SAMPLE:
  print(make_chain(helper.shuffle_list(arr)))
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
  n = helper.get_random(1,2,100)
  words = [helper.WORDS[x] for x in helper.get_unique_random(n,0,127141)]
  # Result
  START = datetime.datetime.now()
  res = make_chain(words)
  END = datetime.datetime.now()
  TIME.append(END-START)
  # File write
  if res!='0': print(i,res)
  input_line = str(len(words)) + '\n' + ' '.join(iter(words))
  output_line = res
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print('Time:',sum(TIME,datetime.timedelta(0)))