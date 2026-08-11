# 导入模块      调用方式:模块名.功能名
import random
print(random.randint(1, 10))
import random as rnd
print(rnd.randint(1, 10))

# 导入模块中的功能      调用方式:功能名
from random import randint
print(randint(1, 10))
from random import randint as rnd
print(rnd(1, 10))
from random import *
print(randint(1, 10))