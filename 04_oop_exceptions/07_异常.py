#异常
# 异常(也称为bug)就是程序运行过程中出现的错误,它会中断程序的正常执行流程
# 作用:
# 保证数据,逻辑的正确性,避免程序执行混乱
# 在开发阶段,尽量发现更多的问题,尽早解决问题,保障程序正常执行
#
# #出现异常有两种处理方案:
# 1.不做处理:整个程序因为一个bug,中断执行
# 2.捕获异常:按照我们自己的处理方式,处理完异常,程序继续执行(编写程序是,做好预案,出现异常,按预案处理)
#
# try:
#   可能出现异常的业务代码1
#   可能出现异常的业务代码2
#   ...
# except [异常类型 as 变量名]
#   出现异常时的原
# [finally:
#   不管是否出现异常,都会执行的代码]
# try:
#     print("=============")
#     # print(my_name)                  #运行错误,报错信息: name 'my_name' is not defined
#     # print(1/0)                      #运行错误,报错信息: division by zero
#     print("abc"[10])                    #程序运行出错,错误信息: string index out of range
#     print("=============")
# except NameError as e:              #捕获NameError异常
#     print("运行错误,报错信息:",e)
# except ZeroDivisionError as e:
#     print("运行错误,报错信息:",e)
# except Exception as e:              #捕获所有异常
#     print("程序运行出错,错误信息:",e)
# finally:                            #无论程序是否正常运行,finally代码块中的代码都会正常运行
#     print("释放资源~")

#异常的传递
#异常传递就是异常在函数调用中层层上报的过程,知道有人处理它,或者程序崩溃

def func1():
    print("func1...running...")
    func2()

def func2():
    print("func2...running...")
    func3()

def func3():
    print("func3...running...")
    print(my_name)

if __name__ == "__main__":
    try:
        func1()
    except Exception as e:
        print("程序运行出错,错误信息:",e)
