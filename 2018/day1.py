import sys
from itertools import accumulate, cycle
from helpers import read_numbers

def partTwo(f):
  mySet = {0}
  return next(freq for freq in accumulate(cycle(f)) if freq in mySet or mySet.add(freq))

def partOne(f):
  return sum(f, 0)

def solution(fileName):
  frequency_list = read_numbers(fileName)
  return ("Solution 1:", partOne(frequency_list) ), ("Solution 2:", partTwo(frequency_list))

if __name__ == '__main__' :
  print(solution(sys.argv[1]))