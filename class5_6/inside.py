def find_even_number(n, m):
    numbers = [i for i in range(n, m + 1)]
    center = int((n + m) / 2)
    for i in numbers:
        if i % 2 != 0:
            continue
        result = "짝수" if i != center else "중간값"
        print(f"{i} {result}")


# 입력값 유효성 확인
try:
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))

    if n < 1 or m < 1 or n > m:
        raise Exception()
except:
    print("입력 정보가 옳지 않습니다")
    quit()

# 함수 수행
find_even_number(n, m)
