from helpers import read_strings
from collections import deque
import string
def oppostiePolar(a, b):
  if a in string.ascii_lowercase:
    if a.upper() == b:
      return True
  elif a in string.ascii_uppercase:
    if a.lower() == b:
      return True

  return False
def react(polymer):
  d = deque()
  d.append(polymer[0])
  for letter in polymer[1:]:
    if len(d) == 0:
      d.append(letter)
    elif oppostiePolar(d[-1], letter):
      d.pop()
    else:
      d.append(letter)
      
  return len(d)
def func(s, polymer):
  for i in s:
    yield react(polymer.replace(i, '').replace(i.swapcase(), ''))

def partOne(polymer):
  return react(polymer)
def partTwo(polymer):

  s = set(polymer)

  return min(func(s, polymer))
      

if __name__ == '__main__':
  POLYMER = read_strings('input_day5.txt')
  print(partOne(POLYMER[0]), partTwo(POLYMER[0]))