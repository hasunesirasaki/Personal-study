import random

#def number(n)


x = random.sample(range(10),3)
y = random.randrange(10)
z = random.randrange(10)

data1 = x[0]
data2 = x[1]
data3 = x[2]

num = (data1,data2,data3)
print(num)
while True:
    a = int(input("答えは"))
    if a == num:
        print("正解")
    else:
        print(num)
        break
