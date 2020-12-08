import re
from collections import defaultdict
from util import getLinesFromFile

isIn = defaultdict(set)

def breakdownBags(line):
  root, children = line.split('contain')
  root = root.rstrip('s ')
  for childBag in [match[2] for match in re.findall(r'((\d (\w+ \w+ bag)s?)[.,])+',children)]:
    isIn[childBag].add(root)

def getContainers(bag):
  containedIn = isIn[bag]
  return containedIn.union(c2 for c in containedIn for c2 in getContainers(c))

input = getLinesFromFile('input.txt')

[breakdownBags(line) for line in input]

print(len(getContainers('shiny gold bag')))