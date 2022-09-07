import random

# 파이썬은 호이스팅이 없다


def valueCheck(val):
    if val == "가위" or val == "0":
        result = 0
    elif val == "바위" or val == "1":
        result = 1
    elif val == "보" or val == "2":
        result = 2
    else:
        print("올바른 값이 아닙니다")
        quit()
    return result


def changeWord(val):
    if val == 0:
        word = "가위"
    elif val == 1:
        word = "바위"
    else:
        word = "보"
    return word


def rspGame(computer, user):
    result = computer - user
    print("나: ", changeWord(user))
    print("컴퓨터: ", changeWord(computer))
    if result == 0:
        print("비김")
    elif result == -2 or result == 1:
        print("컴퓨터 승리")
    else:
        print("유저 승리")


computer = random.randint(0, 2)
user = valueCheck(input("가위 바위 보! "))
rspGame(computer, user)
