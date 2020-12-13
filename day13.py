from util import getLinesFromFile
from math import lcm #requires python39 or higher

input = getLinesFromFile('input.txt')
schedule = input[1].split(',')

idsWithOffset = [(int(x), schedule.index(x)) for x in schedule if x != 'x']

#part 2. part 1 was solved with a calculator.
t=0
s=1
i=0
lcmOf = [idsWithOffset[i][0]]
for i in range(len(idsWithOffset)-1):
    while not((t + idsWithOffset[i][1]) % idsWithOffset[i][0] == 0 and (t + idsWithOffset[i + 1][1]) % idsWithOffset[i + 1][0] == 0):
        t += s
    lcmOf.append(idsWithOffset[i+1][0])
    s = lcm(*lcmOf)
    
print(t)