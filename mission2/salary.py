def yearly_payment(mpay):
    beforeYPay = mpay * 12
    if beforeYPay <= 1200:
        rate = 6
    elif beforeYPay <= 4600:
        rate = 15
    elif beforeYPay <= 8800:
        rate = 24
    elif beforeYPay <= 15000:
        rate = 35
    elif beforeYPay <= 30000:
        rate = 38
    elif beforeYPay <= 50000:
        rate = 40
    else:
        rate = 42

    afterYPay = int(beforeYPay * (1 - rate / 100))
    print("세전 연봉: ", beforeYPay, "만원")
    print("세후 연봉: ", afterYPay, "만원")


monthly_payment = 300
yearly_payment(monthly_payment)
