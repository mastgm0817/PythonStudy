# 상속
# : 클래스들에 중복된 코드를 제거하고 유지보수를
#   편하게 하기 위해서 사용.


# 부모 클래스
class Monster:
    def __init__(self, name, health, attack):  # 생성자
        self.name = name
        self.health = health
        self.attack = attack

    def move(self):
        print(f"{self.name} 지상에서 이동하기")


# 자식 클래스
class Wolf(Monster):  # 괄호안에 상속받을 부모클래스들 넣으면 상속이 가능하다.
    pass  # 몸체를 만들고 싶지 않을때 정의


class Shark(Monster):
    def move(self):  # 메서드 오버라이딩
        print(f"{self.name} 헤엄치기")


class Dragon(Monster):
    def move(self):  # 메서드 오버라이딩
        print(f"{self.name} 날아다니기")


wolf = Wolf("늑대", 500, 50)
shark = Shark("상어", 1000, 100)
dragon = Dragon("용", 5000, 550)


wolf.move()
shark.move()
dragon.move()
