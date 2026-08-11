__all__ = ['PI','log_separator1',  'log_separator4']

PI = 3.1415926

def log_separator1():
    print('-'*30)

def log_separator2():
    print('+'*30)

def log_separator3():
    print('#'*30)

def log_separator4():
    print('*'*30)


#测试函数
# __name__:Python中的内置变量,表示的是当前模块的名字(直接运行当前模块,__name__的值为"__main_"),作为模块被导入时,__name__的值就是模块名称
# print(__name__)     #__main__
#执行当前文件则会执行如下代码,当做模块导入,如下代码不会执行
if __name__ == '__main__':          #直接输入main会跳出if __name__ == '__main__':
    log_separator1()
    log_separator2()
    log_separator3()
    log_separator4()



# log_separator1()
# log_separator2()
# log_separator3()
# log_separator4()