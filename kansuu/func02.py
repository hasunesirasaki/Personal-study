# 消費税　関数の引数と戻り値１

def tax(p):
    price = p * 1.08 # 消費税８％
    return price


pay = tax(100)
print (pay,"円")
