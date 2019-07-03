import requests
import json

URL = "http://weather.livedoor.com/forecast/webservice/json/v1"
location_id = "130010"
r = requests.get(URL + "?city=" + location_id)
msg = json.loads(r.content)
#print(msg)


#print(msg["forecasts"]) #予報
print(msg["title"])  #ページタイトル
print(msg["location"]) #場所
#print(msg["description"]["text"]) #概況
