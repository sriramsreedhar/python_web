from urllib2 import urlopen
html = urlopen("http://www.ndtv.com")
print(html.read())
