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
alpha_list = list(string.ascii_uppercase)

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

def mul(word1, word2):
  return word1 * alpha_list.index(word2)

def find_depth(exp):
  num = 0
  while ParseNestedParen(exp, num) != "Fail":
    num += 1
  return num

def get_string(string, operand):
  pos = string.find(operand)
  start = pos
  end = pos
  while (string[start] != "+") or (string[start] != "-") or (start != 0):
    start -= 1
  while (string[end] != "+") or (string[end] != "-") or (end != len(string)) or (string[end] != "*"):
    end += 1
  return (start, end)

def do_operation(string, operand):
  word1, word2 = string[:string.find("+")], string[string.find("+"):]
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
    string_to_work_on = ParseNestedParen(temp_exp, depth)
    ans = string_to_work_on
    while "*" in string_to_work_on:
      start, end = get_string(string_to_work_on, "*")
      slice_ans = do_operation(string_to_work_on[start : end], "*")
      ans = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
    while "-" in string_to_work_on:
      start, end = get_string(string_to_work_on, "-")
      slice_ans = do_operation(string_to_work_on[start : end], "-")
      ans = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
    while "+" in string_to_work_on:
      start, end = get_string(string_to_work_on, "+")
      slice_ans = do_operation(string_to_work_on[start : end], "+")
      ans = string_to_work_on.replace(string_to_work_on[start:end], slice_ans)
    
    string_to_work_on = "(" + string_to_work_on + ")"
    temp_exp = temp_exp.replace(string_to_work_on, ans)

    depth -= 1
  return temp_exp


# Sample cases
print()
SAMPLE = [
  '((a*c)+b)', '(a+c)', '(a-c)', '((a*c)+c)'
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