
from urllib2 import urlopen
from bs4 import BeautifulSoup

#You can use this beautiful soup module to view just any or all of body,body.h1, body.h2, div etc...

html = urlopen("http://www.ndtv.com")
bsObj = BeautifulSoup(html.read(),"html.parser")
#print(bsObj.h1)
#print(bsObj.h2)
#print(bsObj.h3)
#print(bsObj.h4)
#print(bsObj.body)
#view just title of website
print(bsObj.title)



#Result looks like
#sh-3.2# python beautiful_soup.py
#<title> 	NDTV: Latest News, India News, Breaking News, Business, Bollywood, Cricket, Videos &amp; Photos </title>
#sh-3.2#
