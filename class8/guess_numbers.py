import random


def guess_numbers():
    answer_list = get_numbers()
    check_list = [i for i in range(0, 101)]
    finish_flag = 3
    round = 0

    check_list[answer_list[0]] = "최솟값"
    check_list[answer_list[1]] = "중간값"
    check_list[answer_list[2]] = "최댓값"

    # 정답확인
    # print(answer_list)

    while True:

        # 정답을 찾을 때마다 flag 값을 1점 깍는다. 0점이 되면 종료.
        if finish_flag == 0:
            break

        round += 1
        print(f"{round}차 시도")

        predict_num = get_user_number()

        # 정답확인 분기
        if check_list[predict_num] == -1:
            print("이미 예측에 사용한 숫자입니다")
        else:

            # isinstance : str 타입인 경우 True 리턴
            if isinstance(check_list[predict_num], str):
                print(f"숫자를 맞추셨습니다! {predict_num}는 {check_list[predict_num]}입니다.")
                finish_flag -= 1
            else:
                print(f"{predict_num} 은/는 없습니다")

            check_list[predict_num] = -1

        # 힌트제공 분기
        if round == 5 or round == 10:
            if predict_num > answer_list[0]:
                print(f"최솟값은 {predict_num} 보다 작습니다")
            elif predict_num < answer_list[2]:
                print(f"최대값은 {predict_num} 보다 큽니다")

    print(f"게임종료\n{round}번 시도만에 예측 성공")


# 1~100 사이 사용자값 리턴
def get_user_number():
    try:
        predict_num = int(input("숫자를 예측해보세요 : "))

        if predict_num < 0 or predict_num > 100:
            raise Exception()
    except Exception:
        print("1~ 100사이 정수값을 입력해 주세요")
        quit()

    return predict_num


# 중복되지 않는 3개의 숫자가 담긴 list 리턴 (정렬)
def get_numbers():
    numbers = {}

    while True:
        if len(numbers) >= 3:
            break

        numbers[random.randint(0, 100)] = None

    return sorted(numbers)


guess_numbers()
