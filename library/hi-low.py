# 数当てゲーム
import random
num = random.randrange(100)
cnt = 0;
print ("数当てゲーム")
while True:
    cnt +=1
    x = int(input("NUM?>"))
    if x == num:
        print(x, "は正解")
        print(cnt, "回で正解しました")
        break
    elif x < num:
        print(x, "よりも大きい")
    elif x > num:
        print(x, "よりも小さい")
