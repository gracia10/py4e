import math


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


def count_prime_number(n, m):
    numbers = [i for i in range(n, m + 1)]
    count = 0
    for n in numbers:
        if is_prime_number(n):
            count += 1
    print(f"소수개수 {count}")


n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)
