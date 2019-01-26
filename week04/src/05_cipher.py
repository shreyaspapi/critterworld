import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
PROBLEM_NUM = '05' # Change according to problem number in contest

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