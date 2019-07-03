# omikuzi
import random
msg = ("大吉","中吉","小吉","吉","凶","大凶")
name = int(input("名前は"))

print(name , "さんの運勢は" , random.choice(msg) , "です")
