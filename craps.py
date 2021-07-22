#Craps Game
# 주사위 두개를 굴린다
# 굴린 주사위 합이 7, 11이면 승리, 2,3,12면 진다
# 4,5,6,8,9,10이 나오면 다시 주사위를 굴리고,
# 처음 굴렸던 주사위 합이 나오면 승리하고,
# 처음 굴렸던 주사위 합이 나오기 전에 합이 7이 나오면 진다.

from random import *

dice1=randint(1,6)
dice2=randint(1,6)

print("처음 굴린 주사위1: "+str(dice1))
print("처음 굴린 주사위2: "+str(dice2))

while(1):
    if (dice1+dice2==7) | (dice1+dice2==11):
        print("승리")
        break
    elif (dice1+dice2==2) | (dice1+dice2==3) | (dice1+dice2==12):
        print("패배")
        break
    else:
        while(1):
            dice1_new=randint(1,6)
            dice2_new=randint(1,6)
            print("다시 굴린 주사위1: "+str(dice1_new))
            print("다시 굴린 주사위2: "+str(dice2_new))
            if dice1+dice2==dice1_new+dice2_new:
                print("승리")
                break
            elif dice1_new+dice2_new==7:
                print("패배")
                break
            else:
                continue
        break
