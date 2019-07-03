
import io
from html.parser import HTMLParser

class MyHtmlStripper(HTMLParser):
    def __init__(self, s):
        super().__init__()
        self.sio = io.StringIO()
        self.feed(s)

    def handle_starttag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        self.sio.write(data)

    @property
    def value(self):
        return self.sio.getvalue()


import requests
import janome
from bs4 import BeautifulSoup


handle ="earthwata"
r = requests.get("https://twitter.com/"+handle)
if r.status_code == 200:
    soup = BeautifulSoup(r.text,"lxml")
    msgs = soup.find_all("p",class_="tweet-text")
    for i in msgs:
        msg = i
        print(msg)
        print()
else:
    print("Not Found")




# Blogからの本文を取得
url = "http://blog.media.teu.ac.jp/2018/06/post-f5aa.html"
r = requests.get(url)
if r.status_code == 200:
    soup = BeautifulSoup(r.text,"lxml")
    msgs = soup.find_all("div",class_ = "entry-body")
    msgs += soup.find_all("div" ,class_="entry-more-text")
    for i in msgs:
        msg = MyHtmlStripper(str(i)).value
        print(msg)
        print()
else:
    print("Not Found.")
