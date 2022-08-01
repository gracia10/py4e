# 입력값 유효성 확인
try:
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))

    if n < 1 or m < 1 or n > m:
        raise Exception()
except:
    print("입력 정보가 옳지 않습니다")
    quit()

# 찍수,짝수 중앙값 출력
def find_even_number(n, m):
    center = int((n + m) / 2)
    for i in range(n, m + 1):
        if i % 2 != 0:
            continue
        print(f"{i} 짝수")

        if i != center:
            continue
        print(f"{i} 중앙값")


find_even_number(n, m)
