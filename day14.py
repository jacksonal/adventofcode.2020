import re
from util import getLinesFromFile
from collections import defaultdict

def floatingAddressGenerator(splitAddress, currentAddress=''):
  if len(splitAddress) == 1:
    yield currentAddress + splitAddress[0]
  else:
    yield from floatingAddressGenerator(splitAddress[1:], ''.join([currentAddress, splitAddress[0], '0']))
    yield from floatingAddressGenerator(splitAddress[1:], ''.join([currentAddress, splitAddress[0], '1']))

def getFloatingAddress(address, mask):
  binAddress = bin(address)[2:].zfill(36)
  for m in re.finditer('1',mask):
    binAddress = binAddress[:m.start()] + '1' + binAddress[m.start() + 1:]
  for m in re.finditer('X',mask):
    binAddress = binAddress[:m.start()] + 'X' + binAddress[m.start() + 1:]
  return binAddress

mem = defaultdict(int)
input = [line.rstrip('\n') for line in getLinesFromFile('input.txt')]
for line in input:
  if line.startswith('mask'):
    onMask = int(line[-36:].replace('X','0'),2)
    offMask = int(line[-36:].replace('X','1'),2)
  else:
    m = re.match(r'mem\[(\d+)\] = (\d+)', line)
    
    mem[m[1]] = (int(m[2]) | onMask) & offMask

#part1
print(sum(mem.values()))

mem = defaultdict(int)
for line in input:
  if line.startswith('mask'):
    mask = line[-36:]
  else:
    m = re.match(r'mem\[(\d+)\] = (\d+)', line)
    address = getFloatingAddress(int(m[1]), mask)
    value = int(m[2])
    for x in floatingAddressGenerator(address.split('X')):
      mem[x] = value
      
#part2
print(sum(mem.values()))
