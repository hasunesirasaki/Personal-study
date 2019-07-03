# 温度変換の関数

def CtoF(c):
    f = 9/5 * c + 32
    return f

def FtoC(f):
    c = 5/9 * (f-32)
    return c


s = input("摂氏何℃ですか？>")
data = CtoF(float(s))
print(s, "を華氏にすると")
print(data, "°Fです")
