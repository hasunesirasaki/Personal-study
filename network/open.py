#ファイルの書き込み
import requests
URL = "http://www.teu.ac.jp"
FNAME = "index.html"
r = requests.get(URL)
print(r.status_code)
print(r.encoding)
print(r.text)
open(FNAME,"wb").write(r.text.encode("utf-8"))#index(html)ファイルの保存
