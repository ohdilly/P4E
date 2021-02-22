import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


##url ='http://py4e-data.dr-chuck.net/comments_42.xml'
url = ' http://py4e-data.dr-chuck.net/comments_853917.xml'

print('Retrieving: ' + url)
data  = urllib.request.urlopen(url,context=ctx).read()
print('Retrieved', len(data), 'characters')
##print(data.decode())
tree = ET.fromstring(data)
mylist = tree.findall('.//count')
i=0
j=0
for x in mylist:
    j=j+1
    i= i + int(x.text)
print('Count: ' + str(j))
print('Sum: ' + str(i))