from util import getLinesFromFile

def binaryTraverse(instruction, segment):
    if len(instruction) == 0:
        return segment[0]
    nextInstruction = instruction[1:]

    if instruction[0] == 'F' or instruction[0] == 'L':
        return binaryTraverse(nextInstruction, segment[:len(segment)//2])
    else:
        return binaryTraverse(nextInstruction, segment[len(segment)//2:])

passes = getLinesFromFile('input.txt')

seatIds = [(binaryTraverse(bp[:-3], range(128)) * 8) + binaryTraverse(bp[-3:], range(8)) for bp in passes]

print(max(seatIds))

print([(id, id in seatIds) for id in range(35,885) if id not in seatIds]) #range based on my assigned input

