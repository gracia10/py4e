# 이름, 실적
member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [
    [4, 5, 3, 5, 6, 5, 3, 4, 1, 3, 4, 5],
    [2, 3, 4, 3, 1, 2, 0, 3, 2, 5, 7, 2],
    [1, 3, 0, 3, 3, 4, 5, 6, 7, 2, 2, 1],
    [3, 2, 9, 2, 3, 5, 6, 6, 4, 6, 9, 9],
    [8, 7, 7, 5, 6, 7, 5, 8, 8, 6, 10, 9],
    [7, 8, 4, 9, 5, 10, 3, 3, 2, 2, 1, 3],
]


def sales_management(names, records):

    # 팀원별 평균 값 딕셔너리 생성
    results = {}

    for i, name in enumerate(names):

        record = 0

        for month_record in records[i]:
            record += month_record

        results[name] = int(record / 12)

    # 평균 값 기준 역정렬 배열
    sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

    # 1,2등 과 3점 이하인 5,6등 출력
    print(sorted_results)
    print(f"보너스 대상자 {sorted_results[0][0]}")
    print(f"보너스 대상자 {sorted_results[1][0]}")

    if sorted_results[len(sorted_results) - 2][1] < 3:
        print(f"면담 대상자 {sorted_results[len(sorted_results) - 2][0]}")
    if sorted_results[len(sorted_results) - 1][1] < 3:
        print(f"면담 대상자 {sorted_results[len(sorted_results) - 1][0]}")


sales_management(member_names, member_records)
