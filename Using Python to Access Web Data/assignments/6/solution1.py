import json
import urllib


while True:

  address = raw_input("Enter location:")
  if len(address) < 1 : break
  
  print "Retrieving", address
  uh = urllib.urlopen(address)
  data = uh.read()
  #print data
  info = json.loads(data)
 
  print "Retrieved", len(data), "characters"
  
  numbersList = []
  for k in info["comments"]:
    numbersList.append(k["count"])
    
  print "Count:", len(numbersList)    
  print "Sum:", sum(numbersList)
   
  