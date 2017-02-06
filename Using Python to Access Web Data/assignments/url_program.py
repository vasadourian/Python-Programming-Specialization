import urllib
from bs4 import BeautifulSoup
import re

url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174282.html"
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

#print soup
#retrieve all span tags

tags = list(soup('html'))

[int(s) for s in tags.split() if s.isdigit()]



'''for tag in tags:
  j = tag.get('span', None)
  number_list.append(j)

x = sum(number_list)
'''
print type(tags)



