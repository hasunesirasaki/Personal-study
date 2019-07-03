import requests

payload = {"key1":"value","key2":"value2"}
r = requests.get("http://httpbin.org/get",params=payload)
print(r.text)

r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)
