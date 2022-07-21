from datetime import datetime

year = int(input("선생님 몇년생이시죠? 4글자로 답해주세요 "))
birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 "))

print("미국 나이 :: ", datetime.today().year - year + birth)