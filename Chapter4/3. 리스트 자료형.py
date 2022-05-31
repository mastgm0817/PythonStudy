# 1. 리스트 만들기
# - 데이터가 있는 리스트

animals = ["가물치", "벼메뚜기", "비단뱀", "도룡뇽"]

# - 데이터가 없는 리스트

empty = []

# 2. 리스트 조작하기

# - 데이터에 접근하기
# 인덱스는 0부터 시작한다.

print(animals[2])  # 비단뱀을 출력
print(animals[-1])  # 리스트의 마지막 인덱스에 있는 값을 출력하기 위해 -1

# - 데이터 추가하기
animals.append("고라니")
print(animals)


# - 데이터 할당하기

animals[1] = "청개구리"
print(animals)


# - 데이터 삭제하기

del animals[0]
print(animals)


# - 슬라이싱

print(animals[1:3])
print(animals[:])  # 전체 다 가져오기
print(animals[:3])
print(animals[1:])  # 비단뱀 부터 마지막까지


# -리스트 길이

print(len(animals))


# - 리스트 정렬

animals.sort()
print(animals)

animals.sort(reverse=True)  # 거꾸로 정렬하기
print(animals)

# 깃테스트
