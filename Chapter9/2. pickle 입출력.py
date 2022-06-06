import pickle

data = {
  "목표1" : "매일 팔굽혀 펴기 100회",
  "목표2" : "매일 코딩 공부 1시간"
}

file = open("./Chapter9/mydata.pickle", "wb")
pickle.dump(data, file)
file.close()

# 2. pick 파일 파이썬으로 가져오기

file = open("./Chapter9/mydata.pickle", "rb")
data = pickle.load(file)
print(data)
file.close()