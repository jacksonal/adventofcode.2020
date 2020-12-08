from util import getLinesFromFile

def parseLineIntoInstruction(line):
  instr, val = line.rstrip('\n').split()
  return instr, int(val)

def executeInstruction(instruction, pointer, accumulator):
  if instruction[0] == 'nop':
    return pointer + 1, accumulator
  elif instruction[0] == 'acc':
    accumulator += instruction[1]
    return pointer + 1, accumulator
  elif instruction[0] == 'jmp':
    return pointer + instruction[1], accumulator
  
  print(instruction)

def runProgram(program):
  instrPointer = 0
  accumulator = 0
  instructionsRun = set()

  while instrPointer < len(program):
    if instrPointer in instructionsRun:
      print('infinite loop')
      print(accumulator)
      return False
    instructionsRun.add(instrPointer)
    instrPointer, accumulator = executeInstruction(program[instrPointer], instrPointer, accumulator)

  print('program finished')
  print(accumulator)
  return True

input = getLinesFromFile('input.txt')

program = [parseLineIntoInstruction(line) for line in input]

#part1
runProgram(program)

#part2
for instr in [x for x in program if x[0] == 'nop']:
  programCopy = program[:]
  idx = programCopy.index(instr)
  programCopy[idx] = ('jmp',programCopy[idx][1])
  if runProgram(programCopy):
    break

for instr in [x for x in program if x[0] == 'jmp']:
  programCopy = program[:]
  idx = programCopy.index(instr)
  programCopy[idx] = ('nop',programCopy[idx][1])
  if runProgram(programCopy):
    break