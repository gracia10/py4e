def find_even_number(n, m):
    numbers = [i for i in range(n, m + 1)]
    center = int((n + m) / 2)
    for i in numbers:
        if i % 2 != 0:
            continue
        result = "짝수" if i != center else "중간값"
        print(f"{i} {result}")


n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)
