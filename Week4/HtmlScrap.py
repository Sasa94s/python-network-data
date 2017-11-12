#  Read the HTML from the data files below, and parse the data,
#  Extracting numbers and compute the sum of the numbers in the file.
#  Test Cases
#  Enter URL - http://py4e-data.dr-chuck.net/comments_49495.html
#  2302
#  Enter URL - http://py4e-data.dr-chuck.net/comments_42.html
#  2553

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ').rstrip()
html = urlopen(url, context=ctx).read()

# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
sum = 0
for tag in tags:
    # Accumulate the content of a tag
    sum += int(tag.contents[0])
print(sum)
