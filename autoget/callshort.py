from requests.utils import urlparse

fname = "urllist.txt"
data = open(fname).readlines()
for u in data:
    host = urlparse(u).hostname
    print(host+".html")
