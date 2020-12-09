from util import getLinesFromFile
from itertools import combinations

def isValidForPreamble(preamble, value):
  candidateValues = set([sum(x) for x in combinations(preamble,2)])
  return value in candidateValues

def findEncryptionWeakness(pivot, targetValue):
  sizes = range(3,pivot)
  for windowLength in sizes:
    contiguousStart = 0
    while(contiguousStart + windowLength < pivot):
      window = input[contiguousStart:contiguousStart+windowLength]
      if sum(window) == targetValue:
        return min(window) + max(window)
      contiguousStart += 1

input = [int(x) for x in getLinesFromFile('input.txt')]

preambleStart = 0
preambleLength = 25
while(isValidForPreamble(input[preambleStart:preambleStart+preambleLength], input[preambleStart + preambleLength])):
  preambleStart += 1

#part1 answer
print(preambleStart + preambleLength)
invalid = input[preambleStart + preambleLength]

contiguousStart = 0
contiguousLength = 2

while(sum(input[contiguousStart:contiguousStart+contiguousLength]) <= invalid):
  contiguousStart += 1
pivot = contiguousStart

#part2 answer
print(findEncryptionWeakness(pivot,invalid))