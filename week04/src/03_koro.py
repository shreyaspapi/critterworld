'''
## Problem ##
Koro Sensei's one year anniversary as a teacher was fast approaching. The students of his class liked him so much that they wanted to gift him something to commemorate the occasion. However, they could not come up with a good gift so they started focusing on what their sensei liked. One thing he was pleased by was symmetry. He was symmetrical, and so were his lessons. Another thing he liked were complex words made from the english alphabet.
Nagisa then came up with a solution. He suggested that the class build a program so given a string **P** and an integer **n**, the program generates a palindrome with maximum *n additions* to P at the end. The program outputs **0** if a palindrome is not possible. 
(n additions at the end implies n characters can be appended to the end of P)

## Input Format ##
First line: t test cases
Next 2t lines:
String P
Integer n

## Constraints ##
1 ≤ t ≤ 2.5*10^6
1 ≤ |P| ≤ 100
1 ≤ n ≤ |P|/2

## Output Format ##
palindrome or 0
'''

import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '03' # Change according to problem number in contest

# Solution
def is_palindrome(string): 
  return string==helper.reverse(string)

def make_palindrome(string):
  for i in range(0,len(string)):
    if is_palindrome(string[i:]): 
      return string+helper.reverse(string[:i])

def gift_koro(p,n):
  palindrome = make_palindrome(p)
  if len(palindrome) <= len(p) + n: return palindrome
  return 0

# Sample cases
print()
SAMPLE = [
  {'string': 'abcd', 'n': 2},
  {'string': 'abcd', 'n': 3}
]
print('Sample Output:')
for sample in SAMPLE:
  print(gift_koro(sample['string'],sample['n']))
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
  length = helper.get_random(1,10,100)
  n = helper.get_random(1,length//4,length//2)
  alphabets = list(helper.get_random(length//2,1,26))
  alphabets = helper.shuffle_list(alphabets*2)
  string = ''.join([chr(96+x) for x in alphabets])
  # Result
  START = datetime.datetime.now()
  res = gift_koro(string,n)
  END = datetime.datetime.now()
  TIME.append(END-START)
  # File write
  if res: print(i,n,length,res)
  input_line = string + '\n' + str(n)
  output_line = str(res)
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))