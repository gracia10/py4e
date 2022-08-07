origin_text = """안녕하세요.
반갑습니다. 파이썬 공부는 정말 재밌습 니  다.
"""

# 조회 단어 갯수 출력 후 파일 저장
def count_word(text, serach):
    counter = 0
    for word in text.split():
        if word.find(serach) > 0:
            counter += 1

    print(counter)
    save(text)


# 파일 생성 or 조회 후 핸들러 종료
def save(text):
    with open("count_word.txt", "w") as fhand:
        fhand.write(text)


count_word(origin_text, "습니다")
