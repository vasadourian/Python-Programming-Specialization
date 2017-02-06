import re

numList = []

inFile = open('regex_sum_174277.txt')

for line in inFile:
  y = re.findall('[0-9]+', line)
  y = map(int, y)
  numList.append(y)
  
  

numList2 = [x for x in numList if x != []]
numList3 = [item for sublist in numList2 for item in sublist]


print numList3

print sum(numList3)