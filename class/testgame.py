import random  #クラスの内側に設定を書きこむ

class Human():
    RACE = "Human"
    def __init__(self, name):
        self.name = name
        self.maxhp = random.randrange(20,40)
        self.hp = self.maxhp
        self.ap = random.randrange(10)
        self.dp = random.randrange(10)
    def allstatus(self):
        print("name:", self.name)
        print("MAXHP:", self.maxhp)
        print("HP:", self.hp)
        print("AP:", self.ap)
        print("DP:", self.dp)

    def defense(self,pt):
        print(self.name,
        "is damaged:", pt)
        self.hp -= pt
        if self.hp <=0:
            self.dead()

    def heal(self,pt):
        print(self.name,
        "is Healed:", pt)
        self.hp += pt
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def dead(self):
        print(self.name,
        "is DEAD.")
        exit()

class Elf(Human):
    def __init__(self, name):
        super().__init__(name)
        self.maxhp = random.randrange(10,20)
        self.hp = self.maxhp
        self.mp = random.randrange(20)
        #
    def allstatus(self):
        super().allstatus()
        print("MP", self.mp)




me = Human("Sirasu")
you = Human("Ryosuke")

print(me.name,"VS", you.name)
while True:
    me.allstatus()
    you.allstatus()
    cmd = input("CMD> ")
    enemycmd = random.choice(["a","d","h",])
    print("YOU:ENEMY >>", cmd," : " ,enemycmd)
    if self.hp == 0:
        print("lose")
        break
