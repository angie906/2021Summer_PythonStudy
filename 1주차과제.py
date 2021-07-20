from math import *
from random import * 

# 주사위 던지기
dice1=int(random()*6)+1
dice2=randint(1,6)
print("주사위 던지기","\n","주사위 1: ",dice1,"\n","주사위 2: ",dice2,"\n") 



# 계산기
print("실행할 연산의 종류를 입력하세요."+"\n"+"1. 덧셈  "+"2. 뺄셈  "+"3. 곱셈  "+"4. 나눗셈  "+"5. 나머지 구하기")
answer=str(input("연산 종류: "))

if answer=="1":
    cal="덧셈"
    ans=dice1+dice2
elif answer=="2":
    cal="뺄셈"
    ans=dice1-dice2
elif answer=="3":
    cal="곱셈"
    ans=dice1*dice2
elif answer=="4":
    cal="나눗셈" 
    ans=dice1//dice2 # 별찍기를 고려하여 계산 결과로 나눗셈의 몫을 출력한다
else: 
    cal="나머지 구하기"
    ans=dice1%dice2

print(str(cal)+" 결과: "+str(ans))



# 별찍기
print("\n"+"별찍기")
for num in range(0,ans+1):
    for star in range(0,num+1):
        print("*",end='') #end에 빈 문자열을 지정하여 다음 번 출력이 바로 뒤에 오도록 한다
    print(sep="\n") #별도의 출력없이 seperater로 개행을 수행한다
print("\n\n")