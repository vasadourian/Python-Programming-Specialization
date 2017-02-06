import urllib
from bs4 import BeautifulSoup
import re

url = 'http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/comments_174282.html'
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
tags = str(soup('span'))

j = re.findall(r'\d+', tags)
j = map(int, j)
i = sum(j)
print i
