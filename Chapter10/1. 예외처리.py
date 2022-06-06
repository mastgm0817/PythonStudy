# 원화를 입력, 환율 입력 -> 달러값

from decimal import DivisionByZero


won = input("원화금액을 입력하세요. >>>")
dollar = input("환율을 입력하세요. >>>")


try: # 예외가 발생할수 있는 코드
  print(int(won) / int(dollar))
except ValueError as error: # 예외가 발생했을때 실행되는 코드
  print("문자열 예외가 발생했습니다.", error)
except DivisionByZero as error:
  print("나누기 0은 불가능합니다.", error)
else: # 예외가 발생하지 않았을때 실행되는 코드
  print("예외가 발생하지 않았을 때 실행되는 코드")
finally: # 항상 실행되는코드 
  print("이용해주셔서 감사합니다.")