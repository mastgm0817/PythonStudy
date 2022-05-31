chin_ups = []
count = 0

for i in range(1, 8):
    count = int(input(f"{i}일차 턱걸이 횟수 >>>"))
    chin_ups.append(count)

avg = sum(chin_ups) / 7
print(int(avg))
