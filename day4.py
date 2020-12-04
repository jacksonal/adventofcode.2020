from util import getFileContents
from functools import reduce
import re

requiredFields = {
  'byr': lambda year: 1920 <= int(year) <= 2002,
  'iyr': lambda year: 2010 <= int(year) <= 2020,
  'eyr': lambda year: 2020 <= int(year) <= 2030,
  'hgt': lambda height: isValidHeight(re.match(r'(\d+)((cm)|(in))', height)),
  'hcl': lambda color: re.match(r'#[0-9a-f]{6}', color) is not None,
  'ecl': lambda color: re.match(r'(amb)|(blu)|(brn)|(gry)|(grn)|(hzl)|(oth)', color) is not None,
  'pid': lambda id: re.match(r'^\d{9}$', id) is not None,
  #'cid', optional
}

def isValidHeight(reMatch):
  if reMatch is None:
    return False
  if reMatch[2] == 'cm':
    return 150 <= int(reMatch[1]) <= 193
  else:
    return 59 <= int(reMatch[1]) <= 76
  
def buildPassportMap(raw):
  return dict([(m[0], m[1]) for m in re.findall(r'(\w+):(\S+)',raw)])

def hasRequiredFields(passportMap):
  return reduce(lambda a,b: a and b, [f in passportMap for f in requiredFields])

def isPassportValid(passportMap):
  if not hasRequiredFields(passportMap):
    return False
  
  return reduce(lambda a,b: a and b, [requiredFields[key](passportMap[key]) for key in requiredFields])
  
input = getFileContents('input.txt')
passports = input.split('\n\n')

print(len(list(filter(lambda a: hasRequiredFields(a),[buildPassportMap(p) for p in passports]))))
print(len(list(filter(lambda a: isPassportValid(a),[buildPassportMap(p) for p in passports]))))
