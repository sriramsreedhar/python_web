
from urllib2 import urlopen
from bs4 import BeautifulSoup

#You can use this beautiful soup module to view just any or all of body,body.h1, body.h2, div etc...

html = urlopen("http://www.ndtv.com")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.h1)
print(bsObj.h2)
print(bsObj.h3)
print(bsObj.h4)
print(bsObj.body)
