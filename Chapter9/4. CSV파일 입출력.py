# CSV파일
# : 데이터가 콤마로 구분되어지는 형태의 데이터

import csv

data = [
  ["이름","반","번호"],
  ["재석",1,20],
  ["홍철",3,8],
  ["형돈",5,32]
]

file = open("./Chapter9/student.csv","w",newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
  writer.writerow(d)

file.close()