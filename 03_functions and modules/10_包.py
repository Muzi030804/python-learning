# 包学习记录

# 包:本质就是一个文件夹,该文件夹中可以包含若干Python模块(.py文件),文件夹下还包含了一个__init__.py
# 作用:模块文件较多时,用来管理多个模块(包的本质也是模块)

#导入包的模块
import utils.my_func
utils.my_func.log_separator1()
utils.my_func.log_separator2()
utils.my_func.log_separator3()

from utils import my_func
my_func.log_separator1()
my_func.log_separator2()

#使用from utils import * 导入全部模块时,需要在__init__.py中添加'__all__=[]',空值允许导入的模块列表
from utils import *
my_func.log_separator1()
my_func.log_separator2()
print(my_var.PI)

#导入模块中的功能
from utils.my_func import log_separator1
log_separator1()