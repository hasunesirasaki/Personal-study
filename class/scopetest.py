#Scope test

data = "global"
def foo():
    data = "inside"
    print(data)
    for i in range(2):
        data2 = "inside"
        data = "local"
        print(data)
    print(data2)
print(data)
foo()
print(data)
print(data)
