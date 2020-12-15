from collections import defaultdict

spokenNumbers = defaultdict(list)
turn = 0
lastNum = 0
startList = [9,12,1,4,17,0,18]
firstTime = True

for num in startList:
  turn+=1
  spokenNumbers[num].append(turn)
  lastNum = num

while turn < 30000000:
  turn+=1
  if firstTime:
    lastNum = 0
  else:
    lastNum = spokenNumbers[lastNum][-1] - spokenNumbers[lastNum][-2]
  firstTime = lastNum not in spokenNumbers
  #print(f'speaking {lastNum} on turn {turn}')
  spokenNumbers[lastNum].append(turn)
  if turn == 2020:
    print(f'turn 2020: {lastNum}')

print(f'turn 30000000: {lastNum}')
  
