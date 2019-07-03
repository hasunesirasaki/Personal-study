import requests

URL = "http://www.teu.ac.jp"
r = requests.get(URL)

print(r.status_code)
print(r.encoding)
#print(r.text) #テキストを引っ張ってくる
#print(r.headders)#ヘッダーの部分を引っ張ってくる
print(r.headers["Date"])
