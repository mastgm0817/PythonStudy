import random
# 부모 클래스


class Monster:
    max_num = 1000

    def __init__(self, name, health, attack):  # 생성자
        self.name = name
        self.health = health
        self.attack = attack
        Monster.max_num -= 1

    def move(self):
        print(f"{self.name} 지상에서 이동하기")


# 자식 클래스
class Wolf(Monster):  # 괄호안에 상속받을 부모클래스들 넣으면 상속이 가능하다.
    pass  # 몸체를 만들고 싶지 않을때 정의


class Shark(Monster):
    def move(self):  # 메서드 오버라이딩
        print(f"{self.name} 헤엄치기")


class Dragon(Monster):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)
        self.skills = ("꼬리치기", "날개치기", "용의분노")  # 스킬 이름은 변경될일 없기때문에 튜플로 생성

    def move(self):  # 메서드 오버라이딩
        print(f"{self.name} 날아다니기")

    def skill(self):
        print(f"{self.name}이 스킬 {self.skills[random.randint(0,2)]} 을 사용했습니다.")


wolf = Wolf("늑대", 500, 50)
shark = Shark("상어", 1000, 100)
dragon = Dragon("용", 5000, 550)
print(wolf.max_num)

wolf.move()
shark.move()
dragon.move()
dragon.skill()
