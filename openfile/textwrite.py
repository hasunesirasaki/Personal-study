#ファイルの書き込み

fname = "test.txt"
fd = open(fname,"w")
print("hello world" ,file=fd)
fd.write("HELLO WORLD" " ryosuke")
fd.write("ryosuke")
fd.close()
