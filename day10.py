from util import getLinesFromFile
from functools import reduce

def joltDiffPart1(input):
  currentJoltage = 0
  joltDiffs = {1:0, 3:0}
  for joltage in input:
    diff = joltage - currentJoltage
    joltDiffs[diff] += 1
    currentJoltage = joltage

  #account for my device
  joltDiffs[3] += 1
  return joltDiffs[1] * joltDiffs[3]

def countCombos(group):
  length = len(group)
  if length <= 2:
    return 1
  elif length == 3:
    return 2
  elif length == 4:
    return 4
  elif length == 5:
    return 7


input = [int(x) for x in getLinesFromFile('input.txt')]
input.sort()

print(joltDiffPart1(input))

segments = []
lastJump = 0
currentJoltage = 0
input.insert(0,0)
for i in range(len(input)):
  diff = input[i] - currentJoltage
  if diff == 3:
    segments.append(input[lastJump:i])
    lastJump=i
  currentJoltage = input[i]
segments.append(input[lastJump:len(input)])

print(f'{reduce(lambda a,b: a*b, [countCombos(x) for x in segments])} possible combinations')
