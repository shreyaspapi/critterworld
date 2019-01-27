'''
## Problem Statement ##
Mary was a very smart woman. However, she was ahead of her time. She loved someone deeply but the society did not approve of her love. Being very smart, she still managed to send letters to her lover in a way that no one would be able to decipher them. She devised an encryption scheme and shared it with Jane. Now, Mary and Jane could communicate with each other without the worry of anyone finding out what they were saying.
Here is how her encryption worked:
- Mary took the content of her letter and wrote them vertically over n lines
- She made n columns to form a square
- She then rewrote the letter row wise and sent that to Jane
- Jane repeated the procedure of arranging the content in a square
- She then read the square row by row
- Their love was now secure!
Given a string s and an integer n, rearrange the string as described above. There are t test cases with the given constraints.

## Input Format ##
First line: t test cases
Next 2t lines:
n: Size of the square
s: The string to be encrypted

## Constraints ##
1 ≤ t ≤ 10^5
1 ≤ n ≤ 100
|s| = n^2
s will contain only uppercase letters and underscores (_)

## Output Format ##
The encrypted string on a new line for every test case
'''
import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '01' # Change according to problem number in contest

# Solution
def encrypt(plaintext,n):
  ciphertext = ''
  for i in range(n):
    ciphertext += ''.join([plaintext[x] for x in range(i,len(plaintext),n)])
  return ciphertext

# Sample cases
SAMPLE = ['DO_NOT_WORRY_MY_LOVE_SOCIETY_BE_CRUEL_RISE_ABOVE_','ATTACK_AT_DAWN_WHEN_SLEEP']
print(encrypt(SAMPLE[0],7))
print(encrypt(SAMPLE[1],5))


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
  length = helper.get_random(1,2,n*n)
  underscores = n*n - length
  alphabets = list(helper.get_random(length,1,26))
  string = [chr(64+x) for x in alphabets]
  string += [chr(95)] * underscores
  string = helper.shuffle_list(string)
  message = ''.join(string)
  # Result
  START = datetime.datetime.now()
  res = encrypt(message,n)
  END = datetime.datetime.now()
  TIME.append(END-START)
  # File write
  input_line = str(n) + '\n' + message
  output_line = res
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))