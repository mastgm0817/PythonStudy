# 1. import 패키지.모듈
import unit
from unit import item
import unit.character

# unit.character.test()

# 2. from 패키지 import 모듈

# item.test()


# 3. from 패키지 import *
from unit import *  # *를 쓸대는 init 모듈에 작성을 해줘야한다.

character.test()
item.test()
monster.test()


# 4. import 패키지

unit.character.test()
unit.item.test()
unit.monster.test()
