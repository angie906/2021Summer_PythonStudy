class Unit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{} 유닛이 생성되었습니다".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp,self.damage))

class AttackUnit:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        print("{} 유닛이 생성되었습니다".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp,self.damage))
    
    def attack(self,location):
        print("{}:{} 방향으로 적군을 공격합니다.공격력 {}]".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{}:{} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print("{}:현재 체력은 {}입니다".format(self.name,self.hp))
        if self.hp<=0:
            print("{} 유닛이 파괴되었습니다".format(self.name))