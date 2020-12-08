from util import getFileContents
from functools import reduce

def countUniqueChars(word):
    bucket = set(word)
    return len(bucket)

def countUnanimous(group):
    ledger = {}
    count = 0
    listOfPeople = group.split('\n')
    groupCount = len(listOfPeople)
    for person in listOfPeople:
        for yes in person:
            if yes in ledger:
                ledger[yes] += 1
            else:
                ledger[yes] = 1
            if ledger[yes] == groupCount:
                count += 1
    return count

input = getFileContents('input.txt').rstrip('\n')
groups = input.split('\n\n')

counts = [countUniqueChars(g.replace('\n','')) for g in groups]

print(reduce(lambda a,b: a+b,counts))
print(reduce(lambda a,b: a+b,[countUnanimous(g) for g in groups]))