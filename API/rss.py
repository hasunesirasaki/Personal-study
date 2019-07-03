import feedparser
RSS = "https://news.yahoo.co.jp/pickup/rss.xml"
d = feedparser.parse(RSS)

for entry in d["entries"]:
    print("title:", entry.title)
    print("link:",entry.link)
    print()
