from util import getLinesFromFile

def turn(instr, facing):
    turns = instr[1]//90
    if instr[0] == 'R':
        return (facing + turns) % 4
    else:
        return (facing - turns) % 4

def rotate(instr, loc):
    if instr[1] == 180:
        return -loc[0], -loc[1]
    elif (instr[0] == 'R' and instr[1] == 90) or (instr[0] == 'L' and instr[1] == 270):
        return loc[1], -loc[0]
    elif (instr[0] == 'R' and instr[1] == 270) or (instr[0] == 'L' and instr[1] == 90):
        return -loc[1], loc[0]

def moveToWaypoint(times, shipLoc, waypointLoc):
    newLoc = shipLoc
    for i in range(times):
        newLoc = (newLoc[0] + waypointLoc[0], newLoc[1] + waypointLoc[1])
    return newLoc
    
def step(instr, loc, facing):
    if instr[0] == 'L' or instr[0] == 'R':
        return loc, turn(instr, facing)
    elif instr[0] == 'F':
        return step((directions[facing], instr[1]), loc, facing)
    else:
        return movementFuncs[instr[0]](loc,instr[1]), facing

def step2(instr, shipLoc, waypointLoc):
    if instr[0] == 'L' or instr[0] == 'R':
        return shipLoc, rotate(instr, waypointLoc)
    elif instr[0] == 'F':
        return moveToWaypoint(instr[1],shipLoc,waypointLoc), waypointLoc
    else:
        return shipLoc, movementFuncs[instr[0]](waypointLoc,instr[1])


input = getLinesFromFile('input.txt')

movementFuncs = {
    'E' : lambda coord, dist: (coord[0] + dist, coord[1]),
    'S' : lambda coord, dist: (coord[0], coord[1] - dist),
    'W' : lambda coord, dist: (coord[0] - dist, coord[1]),
    'N' : lambda coord, dist: (coord[0], coord[1] + dist),
}
directions = ['E', 'S', 'W', 'N']
facingIndex = 0
currentLocation = (0,0)
instructions = [(line[0],int(line[1:])) for line in input]

#part1
for instr in instructions:
    currentLocation, facingIndex = step(instr, currentLocation, facingIndex)

print(abs(currentLocation[0]) + abs(currentLocation[1]))

#part2
currentLocation = (0,0)
currentWaypointLocation = (10,1)

for instr in instructions:
    currentLocation, currentWaypointLocation = step2(instr, currentLocation, currentWaypointLocation)
    
print(abs(currentLocation[0]) + abs(currentLocation[1]))