fname = "urllist.txt"
data = open(fname).readlines()
print(data)
for u in data:
    print(u.replace("\n",""))
