# 클래스란 속성과 메서드의 집합

# class 클래스 이름:
# def 메서드이름(self):
# 명령 블록


class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed

    def decrease_health(self, num):
        self.health -= num

    def get_health(self):
        return self.health

    def say(self):
        print("나는 몬스터다")


goblin = Monster(800, 120, 130)
goblin.decrease_health(300)
print(goblin.get_health())


# 파이썬에서는 자료형도 클래스다

a = 10
b = "문자열객체"
c = True

print(type(a))
print(type(b))
print(type(c))


print(b.__dir__())  # 문자열에서 사용할수 있는 메서드
