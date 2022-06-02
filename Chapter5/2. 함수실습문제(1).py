# 실습문제 5.2.1
# 다음은 세개의 정수를 인자로 받아, 합계와 평균을 출력해주는 함수이다. 함수를 호출한 결과로 표준 출력이 나오도록
# 함수를 정의해보자.

import random


def printSumAvg(x, y, z):
    sum = x + y + z
    avg = sum/3
    print(f"합계 : {sum} 평균 : {int(avg)}")


printSumAvg(10, 20, 30)


# 실습문제 5.2.2
# 로또에 당첨 되서 퇴사를 하고 싶었던 김로또는 로또 예상번호 추출 프로그램을 파이썬으로 작성하려고 한다.
# 다음 조건에 따라 김로또의 프로그램을 완성해보자.

# 1. 로또번호 6개를 생성한다.
# 2. 로또 번호는 1~45까지의 랜덤한 번호다.
# 3. 6개의 숫자 모두 달라야 한다.
# 4. getRandomNumber() 함수를 사용해서 구현한다.


def getRandomNumber():
    number = random.randint(1, 45)
    return number


def createNumber():
    numbers = []
    count = 1
    while True:
        pick = getRandomNumber()
        if pick in numbers:
            continue
        else:
            numbers.append(pick)
            count += 1
            if count == 7:
                numbers.sort()
                print(numbers)
                break


createNumber()
