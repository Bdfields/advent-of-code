import time
import re
from collections import defaultdict, Counter
from datetime import datetime
from helpers import read_strings

def sleep_minutes(minute_range):
  for minute in minute_range:
    yield len(minute)

def sum_for_day(sleep_schedule):
  for gaurd_sleep_schedule in sleep_schedule:
    yield sum(sleep_minutes(sleep_schedule[gaurd_sleep_schedule]))

def mins_sleep_per_guard(d):
  for i in d:
    yield (i, sum(sum_for_day(d[i])))

def range_for_each_day(d):
  for day in d:
    for i in d[day]:
      yield i
def minutes_each_day(id):
  for i in range_for_each_day(id):
    for j in i:
      yield j
  
def entries(logs):
  token_specification = [
    ('TIME',   r'\d{4}-\d{2}-\d{2}\s*\d{2}:\d{2}'),  # Integer or decimal number
    ('GUARD',   r'\d+'),           # Assignment operator
    ('SLEEP',      r'sleep'),            # Statement terminator
    ('WAKE',       r'wake'),    # Identifiers
  ]

  tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

  for mo in re.finditer(tok_regex, ''.join(sorted(logs))):
    kind = mo.lastgroup
    value = mo.group()
    if kind == 'TIME':
      currentTime = datetime.strptime(value, '%Y-%m-%d %H:%M')
      continue

    yield (kind, currentTime, value)



def partOne(logs):

  mydict = defaultdict(dict)
  for kind, time, value in entries(logs):
    if kind == 'GUARD':
      id=value
    elif kind == 'SLEEP':
      sleepMinute = time.minute
    elif kind == 'WAKE':
      delta = time.minute - sleepMinute
      print('Guard #{} was asleep for {} minutes'.format(id, delta))
      if time.date() not in mydict[id]:
        mydict[id].update({time.date():[]})
        
      mydict[id][time.date()].append(range(sleepMinute, time.minute))

  t = max(mins_sleep_per_guard(mydict), key=lambda x:x[1])
  longest_sleep_guard_id = t[0]

  c = Counter(minutes_each_day(mydict[id]))

  most_common_mins_sleep = dict()
  for v in mydict:
    c = Counter(minutes_each_day(mydict[v]))
    most_common_mins_sleep[v] = (v, c.most_common(1)[0])

  most_freq_sleep_same_minute = max(most_common_mins_sleep.values(), key=lambda x: x[1][1])

  return (('{} * {}'.format(most_common_mins_sleep[longest_sleep_guard_id][1][0], int(longest_sleep_guard_id)), 
                                                  most_common_mins_sleep[longest_sleep_guard_id][1][0] * int(longest_sleep_guard_id)), 
                                                  
                                                  
                                                  (('{} * {}'.format(int(most_freq_sleep_same_minute[1][0]), int(most_freq_sleep_same_minute[0])), 
                                                 int(most_freq_sleep_same_minute[1][0]) * int(most_freq_sleep_same_minute[0]))))

if __name__ == '__main__':
  start_time = time.time()
  LOGS = read_strings('input_day3.txt')
  print(partOne(LOGS)) 
  print("--- %s seconds ---" % (time.time() - start_time))
