# 입력값 유효성 확인
try:
    n = int(input("첫 번째 수 입력 : "))
    m = int(input("두 번째 수 입력 : "))

    if n < 1 or m < 1 or n > m:
        raise Exception()
except Exception:
    print("입력 정보가 옳지 않습니다")
    quit()

# 범위 내 소수 갯수 확인
def count_prime_number(n, m):
    count = 0

    for number in range(n, m + 1):

        if number == 1:
            continue

        is_prime = 1
        for i in range(2, number):
            if number % i == 0:
                is_prime = 0
                break

        count += is_prime

    print(f"소수개수 {count}")


count_prime_number(n, m)
