# 6명의 회원이고 "아이디,나이,전화번호,성별,지역,구매횟수" 순서로 입력되어 있음
INFO = "abc,21세,010-1234-5678,남자,서울,5,cdb,25세,x,남자,서울,4,bbc,30세,010-2222-3333,여자,서울,3,ccb,29세,x,여자,경기,9,dab,26세,x,남자,인천,8,aab,23세,010-3333-1111,여자,경기,10"


def good_customer(info_string):
    """6명의 회원정복와 VIP를 출력하는 함수"""

    info_split_list = info_string.split(",")
    results = {"아이디": [], "나이": [], "전화번호": [], "성별": [], "지역": [], "구매횟수": []}
    vips = []

    for i in range(0, len(info_split_list), 6):
        customer = [_, _, phone, _, _, count] = info_split_list[i : i + 6]

        # vip 체크
        if int(count) >= 8 and phone != "x":
            vips.append(customer)

        # 전화번호 값 보정
        if phone == "x":
            customer[2] = "000-0000-0000"

        # 회원정보 저장
        for i, key in enumerate(results.keys()):
            results[key].append(customer[i])

    # 회원정보 및 vip 정보 출력
    print(results)

    for vip in vips:
        print(
            f"쿠폰을 받을 회원정보 아이디: {vip[0]}, 나이: {vip[1]}, 전화번호: {vip[2]}, 성별: {vip[3]}, 지역: {vip[4]}, 구매횟수: {vip[5]}"
        )


good_customer(INFO)
