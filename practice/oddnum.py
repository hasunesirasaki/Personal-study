def oddnum(n):
    ans = 1
    n = n+1
    for i in range(1,n,2):
        ans = ans * i
    return ans

n = int(input("Number>>"))
x = oddnum(n)
print(x)
