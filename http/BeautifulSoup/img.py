#リス形式でIMGタグが取り出される

import requests
from bs4 import BeautifulSoup
import os, time, requests

URL = "http://blog.media.teu.ac.jp/"

data = requests.get(URL)
soup = BeautifulSoup(data.text,"lxml")



print(soup.find_all("img"))
#print(soup.find("img")) #ひとつだけ取り出す
print(soup.img.get("src"))
print("--------------------------------------")
print(soup.find("img").get("src")) #画像一枚のみ

#ファイル名の切り出し→URLを分解する

imageurl = soup.find_all("img")[1].get("src")
#print(imageurl.rsplit("/",1)[1].split("?")[0])

#パス名の取り出し
from urllib.parse import urlparse
print(urlparse(imageurl).path) #パス名の取り出し
print(urlparse(imageurl).hostname) #ホストネーム名の取り出し

#画像ファイルの取得と保存

host = urlparse(imageurl).hostname
os.mkdir(host)
print(host)
fname =urlparse(imageurl).path.rsplit("/",1)[1]
print(fname)
imagedata = requests.get(imageurl)
open (host,"wb").write(imagedata.content)
