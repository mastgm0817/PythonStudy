# 내장 모듈
# : 파이썬 설치 시 자동으로 설치되는 모듈

# import math
from math import pi, ceil
import pyautogui as pg
print(pi)
print(ceil(2.7))

# 외부 모듈
# : 다른 사람이 만든 파이썬 파일 pip로 설치해서 사용
# pyautogui
# pip install piautogui

pg.moveTo(500, 500, duration=2)  # 화면에 500,500 위치로 2초동안 이동해라
