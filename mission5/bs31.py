import random


def bs31():
    """31을 외치면 당첨이 되는 함수 (턴당 최대 3회 제시가능)"""

    print("베스킨라빈스 써리원 게임")
    finish_num = 31
    current_num = 0

    while True:

        # 사용자 숫자 입력
        current_num = get_my_number(current_num)
        print(f"현재 숫자: {current_num}")

        # 사용자 숫자가 종료 숫자를 넘은 경우 종료
        if current_num >= finish_num:
            print("사용자 당첨")
            quit()

        # 컴퓨터 숫자 입력
        computer_nums = [current_num + i + 1 for i in range(0, random.randint(1, 3))]

        # 컴퓨터 숫자가 종료 숫자를 넘은 경우 종료
        for computer_num in computer_nums:
            current_num = computer_num
            print(f"컴퓨터 : {current_num}")

            if current_num >= finish_num:
                print("컴퓨터 당첨")
                quit()

        # 승자가 안나온 경우 출력
        print(f"현재 숫자: {current_num}")


def get_my_number(current_num):
    """사용자 입력값 중 마지막값 리턴"""

    # 입력값이 1~3개가 아니거나, 현재값보다 1 크지 않으면 다시 값을 받음
    while True:
        try:
            my = input("My turn - 숫자를 입력하세요: ")
            my_list = my.split()

            if len(my_list) < 1 or len(my_list) > 3:
                raise Exception("입력값 갯수가 옳지 않습니다")

            for my_str in my_list:
                my_num = int(my_str)

                if my_num != current_num + 1:
                    raise Exception("입력값이 옳지 않습니다")

                current_num = my_num

            # 입력값 예외가 발생하지 않은 경우 while문 종료
            break
        except Exception as err:
            print(f"{err}(현재값:{current_num})")

    return current_num


# 함수 실행
bs31()
