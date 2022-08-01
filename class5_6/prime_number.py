def count_prime_number(n, m):
    count = 0

    for number in range(n, m + 1):

        if number == 1:
            continue

        flag = 1
        for i in range(2, number):
            if number % i == 0:
                flag = 0
                break

        count += flag

    print(f"소수개수 {count}")


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
count_prime_number(n, m)
