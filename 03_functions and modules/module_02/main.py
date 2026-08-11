#导入模块
import my_func      #直接导入会将 log_separator1() log_separator2() log_separator3() log_separator4()也输出,所以需要__name__判断

#使用模块中的功能
# print(my_func.PI)
# my_func.log_separator1()
# my_func.log_separator2()
# my_func.log_separator3()
# my_func.log_separator4()

#导入自定义模块中的功能
# from my_func import log_separator1,PI
# print(PI)

from my_func import *
print(PI)
log_separator1()
# log_separator2() 会报错 因为__all__中没有 log_separator2()
