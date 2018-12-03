def read_numbers(fileName):
  return parse_file(fileName, int)

def read_strings(fileName):
  return parse_file(fileName, str)

def parse_file(fileName, transform):
  with open(fileName) as fileHandle:
    return[transform(line.strip()) for line in fileHandle]