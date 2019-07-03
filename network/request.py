#requestによるページの取得

import requests
URL = "http://www.teu.ac.jp"
r = requests.get(URL)
print(r.status_code)
print(r.encoding)
print(r.text)
