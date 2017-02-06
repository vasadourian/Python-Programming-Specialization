import urllib
import json
from bs4 import BeautifulSoup
import re
import ssl

url = raw_input('Enter URL: ')
count = raw_input('Enter count: ')
count = int(count)
position = raw_input('Enter position: ')
position = int(position)

scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
uh = urllib.urlopen(url, context=scontext)
data = uh.read()
soup = BeautifulSoup(data)
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
print url_list
print "Retrieving: ", url

n = 1
while n <= count:
  if n == 1:
    newurl = url_list[position - 1]
  else:
    newurl = url_list[position -1 + (100 * (n - 1))]
  print "Retrieving: ", newurl
  scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
  uh = urllib.urlopen(newurl, context=scontext)
  data = uh.read()
  soup = BeautifulSoup(data)
  tags = soup('a')
  for tag in tags:
    tag.get('href', None)
    tag = str(tag)
    tag_list.append(tag)
  url_list = []
  for tagg in tag_list:
    add_tag = re.findall('"([^"]*)"', tagg)
    url_list.append(add_tag)
  url_list = [item for sublist in url_list for item in sublist]
  n += 1

print newurl
