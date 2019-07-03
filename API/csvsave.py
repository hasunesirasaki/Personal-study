import requests
import json,csv

URL = "http://weather.livedoor.com/forecast/webservice/json/v1"
location_id = "130010"
r = requests.get(URL + "?city=" + location_id)
msg = json.loads(r.content)

with open("07090.csv","w",encoding="shift_jis",newline="") as csvfile:
    tenki = csv.writer(csvfile)
    for data in msg["forecasts"]:
        cols = []
        cols.append(data["date"])
        cols.append(data["telop"])
        tenki.writerow(cols)
        print(cols)

        
