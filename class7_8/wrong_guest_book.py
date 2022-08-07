origin_guest_book = """김갑,123456789
이을,010-1234-5678
박병,010-5678-111
최정,111-1111-1111
정무,010-3333-3333"""


def wrong_guest_book(guest_book):

    save(guest_book)

    for line in guest_book.split():

        # 구조 분해 할당
        [name, phone] = line.split(",")

        if (
            phone.startswith("010")
            and len(phone) == 13
            and len((phone).split("-")) == 3
        ):
            continue

        print(f"잘못 쓴 사람: {name}")
        print(f"잘못 쓴 번호: {phone} \n")


# 파일 생성 or 조회 후 핸들러 종료
def save(text):
    with open("guest_book.txt", "w") as fhand:
        fhand.write(text)


wrong_guest_book(origin_guest_book)
