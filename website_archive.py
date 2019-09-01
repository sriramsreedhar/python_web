#!/usr/local/bin/python3
import webbrowser
import requests

print('Lets find an old website')
site = input("Type a website URL: -")
era = input("Type a Year,Month and Day for eg. 20190818: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s"%(site,era)
response = requests.get(url)
data = response.json()
try:
   old_site = data["archived_snapshots"]["closest"]["url"]
   print("Found this copy: ", old_site)
   print("It should appear in your browser now.")
   webbrowser.open(old_site)
except:
	print("Sorry no luck finding", site)
