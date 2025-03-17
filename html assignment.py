from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

comms = []

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#soup stuff
url = input('Enter URL: ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#find hrefs
tags = soup.find_all("a")

count = int(input("Enter count: "))
pos = int(input("Enter position: ")) - 1

#list spans
for tag in tags:
    comms.append(tag.text)
print("Retrieving: " + url)



#loop
for i in range(count):
    name = comms[pos]
    
    #soup stuff
    url = f'http://py4e-data.dr-chuck.net/known_by_{name}.html'
    print("Retrieving: " + url)
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup.find_all("a")
    
    comms = []
    
    for tag in tags:
        comms.append(tag.text)


print(name)