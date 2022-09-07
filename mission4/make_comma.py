import sys


try:
    NUMBER = int(input("수 입력 : "))
except ValueError:
    print("입력 정보 형식이 숫자가 아닙니다")
    sys.exit()


def make_comma(number):
    """3자리 수마다 , 를 찍는 함수"""

    result = []

    # 절대값 리스트로 변경
    num_string = str(abs(number))
    char_list = list(num_string)

    # 역순으로 조회하여 세번째 자리에 소수점 부여
    char_list.reverse()

    for i, char in enumerate(char_list):
        result.append(char)

        # 마지막 번호에 소수점이 붙지 않아야함
        if i != len(char_list) - 1 and (i + 1) % 3 == 0:
            result.append(",")

    if number < 0:
        result.append("-")

    result.reverse()

    print(*result, sep="")


make_comma(NUMBER)
