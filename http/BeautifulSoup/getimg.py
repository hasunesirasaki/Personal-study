#画像ファイル取得プログラム
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from time import sleep
import requests

URL = "http://blog.media.teu.ac.jp"
pagedata = requests.get(URL)
soup = BeautifulSoup(pagedata.text,"lxml")

i=0
# x+1番目の画像のURLを取得
imgurl = soup.find_all("img")[i].get("src")
print("URL:" , imgurl)
imgfullpath = urlparse(imgurl).path
imgpath = imgfullpath.rsplit("/",1)[1].split("?")[0]
imgfname = imgfullpath.rsplit("/",1)[1].split("?")[0]


# 行末がjpg/gif/pngの時にファイルを取得して保存
if imgfname !="":
    if imgfname.endswith("jpg") or imgfname.endswith("gif") or imgfname.endswith("png"):
        imgdata = requests.get(imgurl)
        open(imgfname,"wb").write(imgdata.content)
        print("Save",imgfname)
