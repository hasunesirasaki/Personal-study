import requests,csv,time
from bs4 import BeautifulSoup


hachioji = "https://weather.yahoo.co.jp/weather/jp/13/4410/13201.html"

data = requests.get(hachioji)
soup = BeautifulSoup(data.content,"lxml")

today_date = soup.find(id="yjw_pinpoint_today").find(class_="yjSt").get_text().strip("_ ")
today_forecast = soup.find(id="yjw_pinpoint_today").find("table")

tomorrow_date = soup.find(id="yjw_pinpoint_tomorrow").find(class_="yjSt").get_text().strip("_ ")
tomorrow_forecast = soup.find(id="yjw_pinpoint_tomorrow").find("table")

week_date = soup.find(id="yjw_week").find(class_="yjMt").get_text().strip("_ ")
week_forecast = soup.find(id="yjw_week").find("table")


with open(time.strftime("%m%d")+".csv","w", newline="", encoding="shift-jis") as csvfile:
    tenkiwriter = csv.writer(csvfile)
    tenkiwriter.writerow((today_date))
    for row in today_forecast.find_all("tr"):
        cols=[]
        for col in row.find_all("td"):
            cols.append(col.get_text().replace("\n",""))
        tenkiwriter.writerow(cols)
        print(cols)

    tenkiwriter2 = csv.writer(csvfile)
    tenkiwriter2.writerow((tomorrow_date))
    for row in tomorrow_forecast.find_all("tr"):
        cols=[]
        for col in row.find_all("td"):
            cols.append(col.get_text().replace("\n",""))
        tenkiwriter2.writerow(cols)
        print(cols)

    tenkiwriter3 = csv.writer(csvfile)
    tenkiwriter3.writerow((week_date))
    for row in week_forecast.find_all("tr"):
        cols=[]
        for col in row.find_all("td"):
            cols.append(col.get_text().replace("\n",""))
        tenkiwriter3.writerow(cols)
        print(cols)
