# 값 입력
input_id = input("주민번호 입력: ")


def check_id(id: str):

    try:
        if len(id) != 14 or id.find("-") != 6:
            raise Exception()

        # 2개 이상의 배열로 split될 경우 Exception 발생
        [front, back] = id.split("-")
        year = int(front[:2])
        gender_number = int(back[0])

        # 00 ~ 21 년생 확인
        if year >= 00 and year <= 21:
            response = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : ")

            # 'o' 응답 중 1,2 로 시작하는 경우 예외 발생
            if response is "o" and gender_number < 3:
                raise Exception()

        gender = "여자" if gender_number % 2 == 0 else "남자"
        print(f"{year}년{front[2:4]}월 {gender}")

    except Exception:
        print("잘못된 번호 입닏다.\n올바른 번호를 넣어주세요")


check_id(input_id)
