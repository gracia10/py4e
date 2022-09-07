# 입력값 유효성 확인
try:
    dan = int(input("몇 단? : "))

    if dan < 1:
        raise Exception()
except Exception:
    print("1 이상의 숫자만 입력해 주세요")
    quit()

# 값이 50 이하인 홀수 구구단
def gugudan(dan):

    print(f"{dan} 단")

    for odd in range(1, 10, 2):
        result = dan * odd
        if result <= 50:
            print(f"{dan} X {odd} = {result}")


gugudan(dan)
