import sys
from itertools import combinations
from helpers import read_strings

def combos_of_n(txt, n):
  return (lst for lst in combinations(txt, n))

def combos_of_any_n(txt, n):
  return (''.join(it)  for it in combos_of_n(txt, n) if len(set(it)) == 1)

def partTwo(lines):
  combo_map = dict()
  for line in lines:
    line = line.strip()
    for i in combinations(line, len(line) -1):
      combo_str = ''.join(i)
      if combo_str in combo_map and line != combo_map[combo_str]:
        return (combo_str)
      else:
        combo_map[combo_str] = line

def partOne(box_ids):
  doubles = set()
  triples = set()

  for count, box_id in enumerate(box_ids,1):
    three_of_any = combos_of_any_n(box_id, 3)

    for it in three_of_any:
      triples.add(count)
      box_id = ''.join(sorted(box_id)).replace(it, '')

    two_of_any = combos_of_any_n(box_id, 2)

  doubles.add(count) if any(True for i in two_of_any) else None

  return len(doubles) * len(triples)

def solution(fileName):
  lines = read_strings(fileName)
  return ("Part 1: ", partOne(lines)), ("Part 2: ", partTwo(lines))

if __name__ == '__main__':
  print(solution(sys.argv[1]))
