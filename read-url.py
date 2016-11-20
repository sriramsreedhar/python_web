from urllib2 import urlopen
html = urlopen("http://www.nytimes.com")
print(html.read())
