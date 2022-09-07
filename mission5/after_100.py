from operator import truediv


# 날짜를 넣으면 100일 뒤가 몇월 며칠인지 계산해주는 함수를 만들어 보겠습니다.
def after_100(month, day, dow):
    counter = 100
    last_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while True:

        this_month_last_day = last_days[month - 1] - day + 1
        next_month_last_day = (
            last_days[month] + last_days[month + 1] + last_days[month + 2]
        )

    print(f"이번달 남은일", this_month_last_day, "das", next_month_last_day)


after_100(6, 1, "월")
# 6월 21일 월요일부터 100일 뒤는 9월 28일 화요일
