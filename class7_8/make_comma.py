# 입력값 유효성 확인
try:
    number = int(input("수 입력 : "))
except ValueError:
    print("입력 정보가 옳지 않습니다")
    quit()


# 3자리 수마다 , 를 찍는 함수
def make_comma(number):
    result = []

    num_string = str(abs(number))
    char_list = [char for char in num_string]

    # FIXME reverse 제거 하고 -index 로 수정 --------
    char_list.reverse()

    for i in range(0, len(char_list)):
        result.append(char_list[i])

        # 마지막 번호가 아닌 3번째 자리
        if i != len(char_list) - 1 and (i + 1) % 3 == 0:
            result.append(",")

    if number < 0:
        result.append("-")

    result.reverse()
    # --------------------------------------------

    print(*result, sep="")


make_comma(number)
