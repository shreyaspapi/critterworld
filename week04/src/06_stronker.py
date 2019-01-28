'''
## Problem Statement ##

## Input Format ##

## Constraints ##

## Output Format ##
'''
import os
import datetime
import helper
from helper import TEST_DIR, INPUT_DIR, OUTPUT_DIR, INPUT_PRE, OUTPUT_PRE, FILE_EXT
import re

PROBLEM_NUM = '' # Change according to problem number in contest

def ParseNestedParen(string, level):
    """
    Generate strings contained in nested (), indexing i = level
    """
    if len(re.findall("\(", string)) == len(re.findall("\)", string)):
        LeftRightIndex = [x for x in zip(
        [Left.start()+1 for Left in re.finditer('\(', string)], 
        reversed([Right.start() for Right in re.finditer('\)', string)]))]

    elif len(re.findall("\(", string)) > len(re.findall("\)", string)):
        return ParseNestedParen(string + ')', level)

    elif len(re.findall("\(", string)) < len(re.findall("\)", string)):
        return ParseNestedParen('(' + string, level)

    else:
        return 'Fail'

    return [string[LeftRightIndex[level][0]:LeftRightIndex[level][1]]]

import string
alpha_list = list(string.ascii_lowercase)

def add(word1, word2):
  return word1+word2

def sub(word1, word2):
  word1_temp = 0
  word2_temp = 0
  for i in word1:
    word1_temp -= alpha_list.index(i)
    word1_temp %= 26
  for j in word2:
    word2_temp -= alpha_list.index(j)
    word2_temp %= 26
  return alpha_list[(word1_temp - word2_temp) % 26]

def word_num(word):
  ans = 0
  for i in word:
    ans += alpha_list.index(i)
    ans %= 26
  return ans
def mul(word1, word2):
  word2_num = word_num(word2)
  return word1 * word2_num

def find_depth(exp):
  num = 0
  try:
      while ParseNestedParen(exp, num) != "fail":
          num += 1
  except:
      pass
  return num-1

def get_string(string, operand):
  pos = string.find(operand)
  start = pos-1
  end = pos
  print("string", string)
  while (start != 0) or (string[start] != "+") or (string[start] != "-"):
    if start <= 0:
      start = 0
      break
    start -= 1
  while (end != len(string)) or (string[end] != "+") or (string[end] != "-") or (string[end] != "*"):
    if end == len(string) - 1:
      end = len(string)
      break
    end += 1
  return (start, end)

def do_operation(string, operand):
  word1, word2 = string[:string.find(operand)], string[string.find(operand) + 1:]
  if operand == "+":
    return add(word1, word2)
  elif operand == "-":
    return sub(word1, word2)
  else:
    return mul(word1, word2)

# Solution
def solution(expression):
  temp_exp = expression[:]
  depth = find_depth(expression)
  while depth:
    string_to_work_on = ParseNestedParen(temp_exp, depth)[0]
    ans = string_to_work_on
    while "*" in ans:
      start, end = get_string(string_to_work_on, "*")
      print("String to work on", string_to_work_on[start : end])
      slice_ans = do_operation(string_to_work_on[start : end], "*")
      ans = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
    while "+" in ans:
      start, end = get_string(string_to_work_on, "+")
      slice_ans = do_operation(string_to_work_on[start : end], "+")
      ans = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
    while "-" in ans:
      start, end = get_string(string_to_work_on, "-")
      slice_ans = do_operation(string_to_work_on[start : end], "-")
      ans = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
    
    string_to_work_on = "(" + string_to_work_on + ")"
    temp_exp = temp_exp.replace(string_to_work_on, ans)
    print("expression", temp_exp)

    depth -= 1
  string_to_work_on = temp_exp
  while "*" in temp_exp:
    start, end = get_string(string_to_work_on, "*")
    print("String to work on", string_to_work_on[start : end])
    slice_ans = do_operation(string_to_work_on[start : end], "*")
    temp_exp = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
  while "+" in temp_exp:
    start, end = get_string(string_to_work_on, "+")
    slice_ans = do_operation(string_to_work_on[start : end], "+")
    temp_exp = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
  while "-" in temp_exp:
    start, end = get_string(string_to_work_on, "-")
    slice_ans = do_operation(string_to_work_on[start : end], "-")
    temp_exp = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
    
  temp_exp = temp_exp.replace(string_to_work_on, ans)
  print("expression", temp_exp)

  return temp_exp


# Sample cases
print()
SAMPLE = [
  '((a*c)+b)'
]
print('Sample output:')
for sample in SAMPLE:
  print(solution(sample))
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
  # Result
  START = datetime.datetime.now()
  res = solution()
  END = datetime.datetime.now()
  TIME.append(START-END)
  # File write
  input_line = ''
  output_line = ''
  if i+1<t:
    input_line += '\n'
    output_line += '\n'
  fin.write(input_line)
  fout.write(output_line)
print("Time:",sum(TIME,datetime.timedelta(0)))