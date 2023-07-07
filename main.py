user_height = float(input("키를 입력해주세요(cm) = "))
user_age = int(input("나이를 입력해주세요 = "))

if user_height >= 150.0 and user_age >= 13:
    print("탑승 가능합니다. 재밌게 즐기세요~")
else:
    print("기준 미달입니다. ")