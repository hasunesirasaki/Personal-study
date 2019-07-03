# 関数の引数と戻り値２ 税抜き価格と税を求める

def reverse_tax(total,pct):
    price = total / (1+pct/100)
    tax = price * (pct/100)
    return price,tax

p,t = reverse_tax(108,8) #108円で消費税８％
print("税抜き価格",p)
print("税",t)
