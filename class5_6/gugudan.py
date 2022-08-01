# 입력값 유효성 확인
try:
    number = int(input("몇 단? : "))

    if number < 1:
        raise Exception()
except:
    print("1 이상의 숫자만 입력해 주세요")
    quit()

# 값이 50 이하인 홀수 구구단
def gugudan(number):

    print(f"{number} 단")

    for i in range(1, 9, 2):
        result = number * i
        if result <= 50:
            print(f"{number} X {i} = {result}")


gugudan(number)
