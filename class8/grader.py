# 학생 답
s = [
    "최정,4245242315",
    "김갑,3242524315",
    "이을,3242524223",
    "박병,2242554131",
    "정무,3242524315",
]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]


def grader(students, answers):
    results = {}

    # 학생별 채점
    for student in students:
        score = 0
        [name, student_answer] = student.split(",")

        for [i, answer] in enumerate(answers):

            if answer == int(student_answer[i]):
                score += 10

        # 점수뱔 학생 목록 저장  ex) - { 90 : '김갑','정무'}
        if results.get(score) is None:
            results[score] = [name]
        else:
            results[score].append(name)

    # 점수 값을 기준으로 역정렬
    sorted_results = sorted(results.items(), reverse=True)
    for i, (score, names) in enumerate(sorted_results):
        for name in names:
            print(f"학생: {name} 점수: {score} {i+1}등")


# 함수 실행
grader(s, a)
