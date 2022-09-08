def after_100(month, date, day):
    """월,일,요일을 입력하면 디데이 뒤 월 , 일 ,요일 정보를 리턴하는 함수"""

    d_day = 200
    weeokdays = ("월", "화", "수", "목", "금", "토", "일")
    calendar = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    origin = (month, date, day)

    month -= 1  # 인덱스 활용을 위해 0~11월로 논리상 약속
    left_day = d_day - 1  # 오늘부터 디데이 카운트 되므로 1제거

    # 잔여일이 매월 막일까지 소요일보다 큰 경우 다음달 1일로 넘긴다  ex) 잔여일 100일 > 6월 막일까지 소요일 9일 -> 7월 1일로 변경
    while True:

        # 막일까지 소요되는 일자 확인
        remove_cnt = calendar[month] - date

        # 디데이 잔여일이 소요일이 보다 작으면 while문 종료. 큰 경우 다음달 1일로 변경
        if left_day - remove_cnt > 0:
            left_day -= remove_cnt + 1
            month = (month + 1) % 12
            date = 1
        else:  # 디데이 잔여일이 막일까지 소요일 적은경우  ex) 잔여일 3일 > 9월 막일가지 소요일 31일
            date += left_day
            break

    print(
        f"{origin[0]}월 {origin[1]}일 {origin[2]}요일부터 {d_day}일 뒤는 "
        f"{month+1}월 {date}일 {weeokdays[((weeokdays.index(day) + d_day - 1) % 7)]}요일"
    )


after_100(6, 21, "화")
# 6월 21일 화요일부터 100일 뒤는 9월 28일 수요일
