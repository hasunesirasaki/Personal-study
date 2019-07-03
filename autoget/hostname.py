import requests

fname = "urllist.txt"
data = open(fname).readlines()
for u in data:
    host = requests.utils.urlparse(u).hostname
    print(host + ".html")
