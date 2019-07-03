import random


def dice(n):
    d = random.randrange(n)+1
    return d
x = dice(10)
print(x)

def dicelist(x,n):
    dlist =[]
    for i in range(n):
        d = dice(x)
        dlist.append(d)
    return dlist
a = dicelist(6,10)
print(a)
