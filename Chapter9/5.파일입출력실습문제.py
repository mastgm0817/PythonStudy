# 실습문제 9.1.1

# 보유한 주식이 목표가에 도달했을 때의 종목별 수익금과 수익률을 출력해주는 프로그램을
# 작성해 보자. mystock.csv 파일로 부터 종목, 매입가, 수량, 목표가 정보를 가져온다.

# 수익금 = (목표가/매입가) * 수량
# 수익률 = (목표가/매입가-1)*100

import csv

# data =[
#   ["종목","매입가","수량","목표가"],
#   ["삼성전자",85000,10,90000],
#   ["NAVER",380000,5,400000]
# ]


# file = open("./Chapter9/mystock.csv","w",newline="", encoding="utf-8-sig")

# writer = csv.writer(file)

# for d in data:
#   writer.writerow(d)

# file.close()

def show_profit(data):
  name = data[0]
  purchase_price = int(data[1])
  target_price = int(data[3])
  quantity = int(data[2])

  profit = (target_price - purchase_price) * quantity
  percentage = (target_price / purchase_price - 1) * 100

  print(f"{name} {profit} {percentage:.2f}%")


file = open("./Chapter9/mystock.csv","r",encoding="utf-8-sig")

reader = list(csv.reader(file))

for data in reader[1:]:
  show_profit(data)
