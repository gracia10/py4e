import random


def checkValue(val):
    if val == "가위" or val == "0":
        result = 0
    elif val == "바위" or val == "1":
        result = 1
    elif val == "보" or val == "2":
        result = 2
    else:
        print("올바른 값이 아닙니다")
        result = -1
    return result


def rsp_advanced(games):
    inputs = {0: "가위", 1: "바위", 2: "보"}
    results = ["비김", "컴퓨터의 승리!", "나의 승리!"]
    current_game = 1

    while True:
        if current_game > games:
            break

        cp = random.randint(0, 2)

        while True:
            my = checkValue(input("가위 바위 보 : "))
            if my != -1:
                break

        print("나: ", inputs[my])
        print("컴퓨터 : ", inputs[cp])
        print(f"----- {games} 번째 판 {results[cp-my]} -----")
        current_game += 1


try:
    games = int(input("몇 판을 진행하시겠습니까? : "))

    if games < 1:
        raise Exception()
except:
    print("1 이상의 숫자만 입력해 주세요")
    quit()

rsp_advanced(games)
