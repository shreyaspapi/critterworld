import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '01' # Change according to problem number in contest

# Solution
def num_palindromes(string,variations):
  pass

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
  length = helper.get_random(1,10,1000)
  n = helper.get_random(1,1,min(100,length//2))
  print(i,n,length)
  alphabets = list(helper.get_random(length,1,26))
  string = ''.join([chr(96+x) for x in alphabets])
  # Result
  START = datetime.datetime.now()
  res = num_palindromes(string,n)
  END = datetime.datetime.now()
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