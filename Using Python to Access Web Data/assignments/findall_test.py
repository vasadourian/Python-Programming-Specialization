import re

astring = [' I am from "houston" ', 'i am from "dallas" ', ' i am from "austin" ']

thislist = []
for aastring in astring:
  j = re.findall('"([^"]*)"', aastring)
  thislist.append(j)

print thislist
