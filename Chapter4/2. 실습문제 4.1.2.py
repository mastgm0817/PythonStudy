from turtle import st


study_hours = int(input("공부시간을 입력하세요(시간)>>>"))

if study_hours >= 10:
    print("휴대폰 잠금 해제")
elif 5 <= study_hours < 10:
    print(" 휴대폰을 30분간 사용가능 합니다.")
else:
    print(" 휴대폰 사용이 불가능합니다.")
