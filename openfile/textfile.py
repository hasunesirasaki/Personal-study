#ファイルを開く
fname = "amenimo.txt"
f = open(r'C:\Users\ryosu\.atom\webpro\openfile,'r',encoding="utf-8_sig")
i=0
for line in f.readlines():
    i += 1
    print(i,line)
