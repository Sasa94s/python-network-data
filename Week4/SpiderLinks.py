#  Extract the href= values from the anchor tags,
#  Scan for a tag that is in a particular position
#  Relative to the first name in the list,
#  Follow that link and repeat the process
#  a number of times and report the last name you find

#  Test Cases
# Enter URL - http://py4e-data.dr-chuck.net/known_by_Rajveer.html
# Enter count - 7
# Enter position - 18
# http://py4e-data.dr-chuck.net/known_by_Rajveer.html
# http://py4e-data.dr-chuck.net/known_by_Rubhan.html
# http://py4e-data.dr-chuck.net/known_by_Montague.html
# http://py4e-data.dr-chuck.net/known_by_Eleni.html
# http://py4e-data.dr-chuck.net/known_by_Innes.html
# http://py4e-data.dr-chuck.net/known_by_Dexter.html
# http://py4e-data.dr-chuck.net/known_by_Dilsa.html
# http://py4e-data.dr-chuck.net/known_by_Damla.html
# Damla
#
#
# Enter URL - http://python-data.dr-chuck.net/known_by_Fikret.html
# Enter count - 4
# Enter position - 3
# http://python-data.dr-chuck.net/known_by_Fikret.html
# http://python-data.dr-chuck.net/known_by_Montgomery.html
# http://python-data.dr-chuck.net/known_by_Mhairade.html
# http://python-data.dr-chuck.net/known_by_Butchi.html
# http://python-data.dr-chuck.net/known_by_Anayah.html
# Anayah

# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ').rstrip()
count = int(input('Enter count - '))
pos = int(input('Enter position - '))-1
names = []
while count >= 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    tags = soup('a')
    print(url)
    # names.append(re.findall('^h\S+//\S+/k\S+y_(\S+).h\S+', url)[0])
    names.append(tags[pos].contents[0])
    url = tags[pos].get('href', None)
    count -= 1
# for name in names:
#     print(name, end=' ')
print(names[count-1])
