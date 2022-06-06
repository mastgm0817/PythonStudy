# 1. 파일 쓰기
# file = open("./Chapter9/data.txt","w",encoding="UTF-8")
# file.write("1. 파이썬 공부 원아와 함께하는 키키호호헤헤 푸히히히 원아는 바보다")
# file.close()

#2 . 파일추가

# file = open("./Chapter9/data.txt","a",encoding="UTF-8")
# file.write("2. She said that she is not that fool")
# file.close()

#3. 파일 읽기

# file = open("./Chapter9/data.txt","r",encoding="UTF-8")
# data = file.read()
# print(data)


#4. 파일 한줄 읽기

file = open("./Chapter9/data.txt","r",encoding="UTF-8")

while True:
  data = file.readline()
  print(data, end="")
  if data == "":
    break
file.close()