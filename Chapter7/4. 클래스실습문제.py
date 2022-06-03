# 실습문제 7.1.1

# 병연은 게임회사에서 개발자로 취직을 하게 되었다.
# 지난주 회의 결과로 신작 MMORPG게임의 아이템 구성안을 만들었다.

# 아이템 공통: 이름, 가격, 무게, 판매하기, 버리기
# 장비 아이템: 착용 효과, 착용하기
# 소모품 아이템: 사용 효과, 사용하기

# 단, 버리기는 버릴 수 있는 아이템만 가능하다.


class Items():
    def __init__(self, name, price, weight, isDroppable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isDroppable = isDroppable

    def sell(self):
        print(f"{self.name}의 아이템을 {self.price}에 판매합니다. ")

    def drop(self):
        if self.isDroppable == True:
            print(f"{self.name}을 버립니다.")
        else:
            print(f"{self.name}은 버릴수 없는 아이템 입니다.")


class Weapon(Items):
    def __init__(self, name, price, weight, isDroppable, effect):
        super().__init__(name, price, weight, isDroppable)
        self.effect = effect

    def use_weapon(self):
        print(f"{self.name}을 착용하였습니다. 추가로 {self.effect}효과를 얻습니다.")


class Stuff(Items):
    def __init__(self, name, price, weight, isDroppable, effect):
        super().__init__(name, price, weight, isDroppable)
        self.effect = effect

    def use_stuff(self):
        print(f"{self.name}을 사용하였습니다. 추가로 {self.effect}효과를 얻습니다.")


sword = Weapon("대검", 5000, 50, True, "민첩함+2")
nife = Weapon("나이프", 1000, 30, False, "민첩함+1")
portion = Stuff("포션", 100, 5, False, "체력+50증가")

sword.use_weapon()
sword.sell()
sword.drop()
nife.drop()

portion.sell()
portion.drop()
portion.use_stuff()
