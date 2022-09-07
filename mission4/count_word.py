ORIGIN_TEXT = """안녕하세요.파이썬
반갑습니다. 파이썬 공부는 정말 재밌습 니  다.
"""


def count_word(origin_text, search):
    """조회 단어 갯수 출력 후 파일 저장"""
    print(origin_text.count(search))

    with open("count_word.txt", "w", encoding="utf-8") as fhand:
        fhand.write(origin_text)


count_word(ORIGIN_TEXT, "파이썬")
