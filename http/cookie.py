import requests

payload = {"key1":"value","key2":"value2"}
r = requests.get("http://httpbin.org/get",params=payload)
print(r.text)

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)


url = "http://www.teu.ac.jp"
r = requests.get(url)
print(r.cookies.keys())
for x in r.cookies.keys():
    print(x, "is", r.cookies.get(x))

url = "http://httpbin.org/cookies"
cookies = dict(cookies_are="working")
r = requests.get(url, cookies=cookies)
print(r.text)
