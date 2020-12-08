import re
from util import getLinesFromFile

contains = {}

def parseContainmentRule(line):
  root, children = line.split('contain')
  root = root.rstrip('s ')
  contains[root] = [(match[3], int(match[2])) for match in re.findall(r'(((\d) (\w+ \w+ bag)s?)[.,])+',children)]

def countBagsIn(bag):
  return sum([b[1] + b[1] * countBagsIn(b[0]) for b in contains[bag]])

input = getLinesFromFile('input.txt')

for line in input:
  parseContainmentRule(line)

print(countBagsIn('shiny gold bag'))
