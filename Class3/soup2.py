from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

position = 18
iter = 7
##url ='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Mohaddesa.html'


for x in range(iter + 1):
    print('Retrieving: ' + url)
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html,  'html.parser')
    tags = soup('a')
    tag = tags[position-1]
    url = tag.get('href', None)
    
