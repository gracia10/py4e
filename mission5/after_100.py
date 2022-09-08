def after_100(month, date, day):
    """월 , 일 , 요일을 입력하면 100일 뒤 월 , 일 ,요일 정보를 리턴하는 함수"""

    results = [month, date, None]
    d_day = 100
    counter = d_day - 1
    days = ("월", "화", "수", "목", "금", "토", "일")
    calendar = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    # 디데이 잔여일이 월별 막일까지 소요일보다 큰 경우 다음달 1일로 넘긴다  ex) 잔여일 100일 > 6월 막일까지 소요일 9일 -> 7월 1일로 변경
    while True:
        # 현재일 기준 막일까지 소요되는 일자 확인
        remove_cnt = calendar[results[0]] - results[1]

        # 디데이 잔여일이 소요일이 보다 작으면 while문 종료. 큰 경우 다음달 1일로 변경
        if counter - remove_cnt <= 0:
            break
        else:
            counter -= remove_cnt + 1
            results[0] += 1
            results[1] = 1

    # 디데이 잔여일이 막일까지 소요일 적은경우  ex) 잔여일 3일 > 9월 막일가지 소요일 31일
    results[1] += counter
    results[2] = days[(days.index(day) + (date + d_day) % 7)]

    print(
        f"{month}월 {date}일 {day}요일부터 {d_day}일 뒤는 {results[0]}월 {results[1]}일 {results[2]}요일"
    )


after_100(6, 21, "월")
# 6월 21일 월요일부터 100일 뒤는 9월 28일 화요일
