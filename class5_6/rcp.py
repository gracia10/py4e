import random

# 입력값 유효성 확인
try:
    games = int(input("몇 판을 진행하시겠습니까? : "))

    if games < 1:
        raise Exception()
except:
    print("1 이상의 숫자만 입력해 주세요")
    quit()

# 가위바위보 입력값 유효성 확인
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


# 전적조회 가위바위보
def rsp_advanced(games):
    inputs = {0: "가위", 1: "바위", 2: "보"}
    messages = ["비김", "컴퓨터의 승리!", "나의 승리!"]
    results = [0, 0, 0]
    current_game = 1

    while current_game <= games:

        cp = random.randint(0, 2)

        while True:
            my = checkValue(input("가위 바위 보 : "))
            if my != -1:
                break

        print("나: ", inputs[my])
        print("컴퓨터 : ", inputs[cp])
        print(f"{current_game} 번째 판 {messages[cp-my]}\n")

        results[cp - my] += 1
        current_game += 1

    print(f"나의 전적: {results[2]}승 {results[0]}무 {results[1]}패")
    print(f"컴퓨터의 전적: {results[1]}승 {results[0]}무 {results[2]}패")


rsp_advanced(games)
