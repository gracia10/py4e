def grader(name, score):
    if score >= 95:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    elif score >= 85:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 75:
        grade = "C+"
    elif score >= 70:
        grade = "C"
    elif score >= 65:
        grade = "D+"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("학생이름 : ", name)
    print("점수 : ", score)
    print("학점 : ", grade)


grader("이호창", 99)
