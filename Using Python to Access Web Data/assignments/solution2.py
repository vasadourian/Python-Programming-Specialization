import urllib
from bs4 import BeautifulSoup
import re

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position)

html = urllib.urlopen(url)
soup = BeautifulSoup(html)
tags = soup('a')

tag_list = []
for tag in tags:
  tag.get('href', None)
  tag = str(tag)
  tag_list.append(tag)

url_list = []
for tag in tag_list:
  add_tag = re.findall('"([^"]*)"', tag)
  url_list.append(add_tag)

url_list = [item for sublist in url_list for item in sublist]
print "Retrieving: ", url

n = 1


print url_list[17]
