import xml.etree.ElementTree as ET

root = ET.fromstring("countrydata.xml")

# Top-level elements
x = root.findall(".")

# All 'neighbor' grand-children of 'country' children of the top-level
# elements
y = root.findall("./country/neighbor")

# Nodes with name='Singapore' that have a 'year' child
w = root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
x = root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
k =root.findall(".//neighbor[2]")

print x
