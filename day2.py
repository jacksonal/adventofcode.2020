from util import getLinesFromFile

def extractTokens(line):
  policy, password = line.split(': ')
  occurance, specialChar = policy.split()
  minOccurance, maxOccurance = occurance.split('-')
  return int(minOccurance), int(maxOccurance), specialChar, password

def isValidPasswordA(floorOccurance, ceilOccurance, specialChar, password):
  charCount = password.count(specialChar)
  return charCount >= floorOccurance and charCount <= ceilOccurance

def isValidPasswordB(positionA, positionB, specialChar, password):
  charInPosA = password[positionA-1] == specialChar
  charInPosB = password[positionB-1] == specialChar

  return (charInPosA and not charInPosB) or (charInPosB and not charInPosA)

lines = getLinesFromFile('input.txt')

passwordData = [extractTokens(x) for x in lines]
validPasswordsA = [x for x in passwordData if isValidPasswordA(x[0],x[1],x[2],x[3])]
validPasswordsB = [x for x in passwordData if isValidPasswordB(x[0],x[1],x[2],x[3])]

print(len(validPasswordsA))
print(len(validPasswordsB))