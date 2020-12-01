import sys
from itertools import combinations

with open('input.txt') as f:
    lines = f.readlines()

numbers = [int(l) for l in lines]

for combo in combinations(numbers,2):
  if combo[0] + combo[1] == 2020:
    print(combo)
    print(combo[0] * combo[1])

for combo in combinations(numbers,3):
  if combo[0] + combo[1] + combo[2] == 2020:
    print(combo)
    print(combo[0] * combo[1] * combo[2])