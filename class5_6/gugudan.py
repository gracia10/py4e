def gugudan(a):
    print(f"{a} 단")
    result = 0
    b = 1
    while True:
        result = a * b

        if result > 50:
            break

        print(f"{a} X {b} = {result}")
        b += 2


# 입력값 유효성 확인
try:
    number = int(input("몇 단? : "))

    if number < 1:
        raise Exception()
except:
    print("숫자만 입력해 주세요")

# 함수 수행
gugudan(number)
