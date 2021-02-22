from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

##url = 'http://py4e-data.dr-chuck.net/comments_42.html'
url = 'http://py4e-data.dr-chuck.net/comments_853915.html'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,  'html.parser')
tots = 0

tags = soup('span')
for tag in tags:
    tots = tots + int(tag.contents[0])

print(tots)