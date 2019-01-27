import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '03' # Change according to problem number in contest

# Solution
def is_palindrome(string):
  for i in range(len(string)//2):
    if string[-(i+1)] != string[i]: return False
  return True

def make_palindrome(string,variations):
  palindrome = list(string)
  for i in range(variations):
    if palindrome[-(i+1)] == palindrome[i]:
      i-=1
      continue
    palindrome[-(i+1)] = palindrome[i]
    string = ''.join(x for x in palindrome)
    if is_palindrome(string): return string
  return '-1'

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
  length = helper.get_random(1,10,20)
  n = helper.get_random(1,length//4,length)
  alphabets = list(helper.get_random(length//5,1,26))
  alphabets = helper.shuffle_list(alphabets*5)
  string = ''.join([chr(96+x) for x in alphabets])
  # Result
  START = datetime.datetime.now()
  res = make_palindrome(string,n)
  END = datetime.datetime.now()
  print(i,n,length,res)
  TIME.append(END-START)
  # File write
  input_line = string + '\n' + str(n)
  output_line = str(res)
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))