import sys

def getLinesFromFile(path):
  with open('input.txt') as f:
    lines = f.readlines()
    return lines
