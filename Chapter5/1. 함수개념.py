# 기본형

# 1. 정의하기
import random
from secrets import randbelow


def printHello():
    print("Hello")

# 2. 호출하기


printHello()


# 매개변수가 있는 함수

def sum(a, b):
    print(a + b)


sum(5, 7)


# 반환값이 있는 함수


def getRandomNumber():
    number = random.randint(1, 10)
    return number


print(getRandomNumber())


# 매개변수와 반환값이 있는 함수

def add(a, b):
    result = a + b
    return result


print(add(5, 6))
