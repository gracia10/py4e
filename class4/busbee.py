def bus_fare(age, method):
    if age < 8 or age >= 75:
        pay = 0
    elif age < 14:
        pay = 450
    elif age < 20:
        pay = 720 if method == "카드" else 1000
    else:
        pay = 1200 if method == "카드" else 1300

    print("나이: ", age)
    print("지불유형: ", method)
    print("버스요금: ", pay)


bus_fare(30, "현금")
