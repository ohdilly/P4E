from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Mohaddesa.html'
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,  'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

