from util import getLinesFromFile
from copy import deepcopy

OCCUPIED = '#'
VACANT = 'L'

def countAdjacentOccupied(row, col, state):
  mask = [
    (row-1, col-1), (row-1, col), (row-1, col+1),
    (row, col-1),                 (row, col+1),
    (row+1, col-1), (row+1, col), (row+1, col+1)
  ]
  count = 0
  for coord in mask:
    if coord[0] < 0 or coord[0] >= len(state) or coord[1] < 0 or coord[1] >= len(state[0]):
      continue
    if state[coord[0]][coord[1]] == OCCUPIED:
      count += 1

  return count

def canSeeOccupied(row,col,state, losFunc):
  coord = (row,col)
  while(True):
    coord = losFunc(coord[0],coord[1])
    if coord[0] < 0 or coord[0] >= len(state) or coord[1] < 0 or coord[1] >= len(state[0]):
      return False
    if state[coord[0]][coord[1]] == OCCUPIED:
      return True
    elif state[coord[0]][coord[1]] == VACANT:
      return False

def countVisibleOccupied(row, col, state):
  mask = [
    lambda r,c: (r-1,c-1), lambda r,c: (r-1,c), lambda r,c: (r-1,c+1),
    lambda r,c: (r,c-1),                        lambda r,c: (r,c+1),
    lambda r,c: (r+1,c-1), lambda r,c: (r+1,c), lambda r,c: (r+1,c+1),
  ]
  count = 0
  for los in mask:
    if canSeeOccupied(row,col,state, los):
      count += 1
  return count

def countOccupied(state):
  return sum([len([seat for seat in row if seat == OCCUPIED]) for row in state])

input = [list(line) for line in getLinesFromFile('input.txt')]

currentState = input
changedSeats = -1

while changedSeats != 0:
  changedSeats = 0
  nextState = deepcopy(currentState)
  for row in range(len(currentState)):
    for seat in range(len(currentState[0])):
      if currentState[row][seat] == VACANT and countAdjacentOccupied(row,seat, currentState) == 0: #empty and no one sitting adjacent
        nextState[row][seat] = OCCUPIED
        changedSeats += 1
      elif currentState[row][seat] == OCCUPIED and countAdjacentOccupied(row,seat, currentState) >= 4: #occupied and 4 or more people in adjacent seats
        nextState[row][seat] = VACANT
        changedSeats += 1
  currentState = nextState

print(countOccupied(currentState))

currentState = input
changedSeats = -1

while changedSeats != 0:
  changedSeats = 0
  nextState = deepcopy(currentState)
  for row in range(len(currentState)):
    for seat in range(len(currentState[0])):
      if currentState[row][seat] == VACANT and countVisibleOccupied(row,seat, currentState) == 0: #empty and no one sitting within line of sight
        nextState[row][seat] = OCCUPIED
        changedSeats += 1
      elif currentState[row][seat] == OCCUPIED and countVisibleOccupied(row,seat, currentState) >= 5: #occupied and 5 or more people in line of sight
        nextState[row][seat] = VACANT
        changedSeats += 1
  currentState = nextState

print(countOccupied(currentState))