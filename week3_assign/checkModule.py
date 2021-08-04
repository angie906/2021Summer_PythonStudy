def adultCheck():
    try: 
        age=int(input("나이를 입력하세요: "))
        if age>19:
            print("구매완료")
        else:
            print("구매할 수 없습니다")
    except ValueError:
        print("Error")