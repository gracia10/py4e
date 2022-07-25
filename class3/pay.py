hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

try:
    fh = float(hours)
    fr = float(rate)
except:
    print("Can't convert float")
    quit()

if( fh > 40) :
    reg = fh * fr
    otp = (fh - 40) * (fr * 0.5)
    result = reg + otp
else:
    result = fh * fr
print("Pay, ", result)
