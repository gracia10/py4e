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


try:
    number = int(input("몇 단? : "))
except:
    print("숫자만 입력해 주세요")

gugudan(number)
