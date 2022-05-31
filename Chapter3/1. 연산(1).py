# 1. 대입 연산
# 변수이름 = 데이터

# 2 2. 산술 연산
# 숫자 연산
x = 5
y = 2

print(f"1. {x + y}")
print(f"2. {x - y}")
print(f"3. {x * y}")
print(f"4. {x / y}")
print(f"5. {x // y}")  # 몫
print(f"6. {x % y}")  # 나머지
print(f"7. {x ** y}")  # 제곱

# 문자열연산
tag1 = "#내꺼하자"
tag2 = "#오늘부터 1일"
tag3 = "#여친생김"

tag = tag1 + tag2 + tag3

print(tag)


message = "우리 모두 파이썬을 사랑합시다.\n" * 5
print(message)

# 복합할당연산자


level = 10
level += 1  # 레벨 1 증가

health = 2000
health -= 300  # 체력 300 감소

attack = 300  # 공격력 1.5배 증가
attack *= 1.5

speed = 420  # 이동속도 50퍼 감소
speed /= 2


print(f"레벨은 {level}, 체력은 {health}, 공격력은 {attack}, 이동속도는 {speed}")
