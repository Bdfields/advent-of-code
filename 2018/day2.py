import sys
from itertools import combinations
from helpers import read_strings

def combos_of_n(txt, n):
  return (lst for lst in combinations(txt, n))

def combos_of_any_n(txt, n):
  return (''.join(it)  for it in combos_of_n(txt, n) if len(set(it)) == 1)

def partTwo(lines):
  pass

def partOne(box_ids):
  doubles = set()
  triples = set()

  for count, box_id in enumerate(box_ids,1):
    three_of_any = combos_of_any_n(box_id, 3)

    for it in three_of_any:
      triples.add(count)
      box_id = ''.join(sorted(box_id)).replace(it, '')

    two_of_any = combos_of_any_n(box_id, 2)

    for i in two_of_any:
      doubles.add(count)
      break

  return len(doubles) * len(triples)

def solution(fileName):
  lines = read_strings(fileName)
  return ("Part 1: ", partOne(lines)), ("Part 2: ", partTwo(lines))

if __name__ == '__main__':
  print(solution(sys.argv[1]))
