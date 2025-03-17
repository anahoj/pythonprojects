#Parses through json data. Collates all numerical values into a list and returns the sum of the numbers and the count of the list

import urllib
import json

numbers = []
count=0
total=0

#url stuff
url = input('Enter location: ')
if len(url) < 1 : 
    url = 'http://py4e-data.dr-chuck.net/comments_2155983.json'
print(f"Retrieving: {url}")
    
#opening url
response = urllib.request.urlopen(url)
content = response.read()
data = content.decode()
print(f"Retrieving {len(data)} characters")

#json stuff
nest = json.loads(data)
comms = nest["comments"]

for pair in comms:
    nb = int(pair["count"])
    numbers.append(nb)
    total += nb
    count += 1
    
    
print(f"Count: {count}")
print(f"Sum: {total}")
