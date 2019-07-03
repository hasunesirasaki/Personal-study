import os, time, requests

URLLIST = "urllist.txt"

def readurl():
    ulist = open(URLLIST).readlines()
    return ulist

def createfolder():
    now = time.strftime("%m%d-%H%M%S")
    os.mkdir(now) #フォルダ作成：
    return now #作ったディレクトリの名前を返す

def saveurl(folder,data):
    print("access",data)
    fname = requests.utils.urlparse(data).hostname + ".html" #セーブするファイルの名前
    savename = folder + "/" + fname
    url = data.strip() #末尾の開業を削除
    r = requests.get(url) #URLにアクセス
    print(url, r.status_code) #アクセスしたいURLとステータスを表示
    open(savename,"wb").write(r.content) #ファイルをセーブ

def main():
    url = readurl()
    folder = createfolder()
    for data in url:
        saveurl(folder,data)
        print(data)
        time.sleep(1)

main()
