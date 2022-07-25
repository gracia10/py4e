def computepay(hours, rate) :
    print("In function ", hours, rate)
    if( fh > 40) :
        reg = fh * fr
        otp = (fh - 40) * (fr * 0.5)
        result = reg + otp
    else:
        result = fh * fr
    return result


hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hours)
fr = float(rate)

print("Pay, ", computepay(hours, rate))