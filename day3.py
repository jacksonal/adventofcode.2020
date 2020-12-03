from util import getLinesFromFile

def isTree(horizontal, mountainSlice):
  return mountainSlice[horizontal % len(mountainSlice)] == '#'

def countTreeCollisions(slope, mountain):
  treeCount = 0
  horizontalIdx = 0

  for mountainSlice in lines[::slope[1]]:
    if isTree(horizontalIdx, mountainSlice):
      treeCount += 1
    horizontalIdx += slope[0]
  return treeCount

lines = getLinesFromFile('input.txt')

print(countTreeCollisions((3,1),lines))

print(
  countTreeCollisions((1,1),lines) *
  countTreeCollisions((3,1),lines) *
  countTreeCollisions((5,1),lines) *
  countTreeCollisions((7,1),lines) *
  countTreeCollisions((1,2),lines) 
)