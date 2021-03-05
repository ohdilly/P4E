import json
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


##url ='http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_853918.json'

print('Retrieving: ' + url)
data  = urllib.request.urlopen(url,context=ctx).read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('item count:', len(info))
##print(json.dumps(info, indent=4))
myList = info['comments']
i=0
j=0
for x in myList:
    j=j+1
    i= i + int(x['count'])
print('Count: ' + str(j))
print('Sum: ' + str(i))