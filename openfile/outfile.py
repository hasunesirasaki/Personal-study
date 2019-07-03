# アウトファイル

outfile = "new.txt"
with open(outfile,"w") as fout:
    while True:
        data = input("#")
        if data == "":
            break
        print(data,file=fout)
