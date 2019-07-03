import random

def dice(n):
    d = random.randrange(n)+1
    return d
x = dice(10)
print(x)

def twodice():
    ans = dice(6)+dice(6)
    return ans
a = twodice()
print(a)

#x = 6
#a = random.sample(range(x),2)
#print(a)
