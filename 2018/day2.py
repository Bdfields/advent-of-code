import sys
import itertools
from helpers import read_strings

def partTwo(lines):
  return lines

def partOne(lines):

  #build a list of all dups I'm testing against

  #get combinations of input line

  #if combination is in the created list count it
  returnUniqueSets = set()
  returnUniqueSets2 = set()
  threes =0;
  twos = 0;

  for line in lines:

    combo = [ lst for lst in itertools.combinations(line, 3) if len(set(lst)) == 1 ]
    print(line)
    s = line
    if len(combo) > 0:
      print(combo)
      threes+=1
      print("threes hit", threes)
      sLine = ''.join(sorted(line))
      s = sLine
      for i in combo:
        s = s.replace(''.join(i),'')
      
      
      print("this is whats left ", s)
    combo2 = [lst for lst in itertools.combinations(s,2) if (len(set(lst)) == 1)]
    if len(combo2):
      print(combo2)
      
      twos+=1
      print("twos hit", twos)
    #combo2 = [ lst for lst in itertools.combinations(comp, 2) if len(set(lst)) == 1 ]
    #if len(combo2) > 0:
        #twos+=1;
        #print("twos hit for line: ", line)

  #print("PartOne", combinations)
  #return lines


  return twos * threes

def solution(fileName):
  lines = read_strings(fileName)
  pass
  return (("Part 1: ", partOne(lines)),("Part 2: ", partTwo(lines)))

if __name__ == '__main__' :
  print(solution(sys.argv[1]))