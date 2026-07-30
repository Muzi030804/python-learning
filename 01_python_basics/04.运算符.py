#  / 除法结果是小数  // 整除，结果是整数  %取余  **幂指数：10**3 = 10的3次方

# #案例  要求输入两个数x，y，分别输出x+y和x-y
# x = input("请输入x：")
# y = input("请输入y：")
# print(f"x+y={float(x)+float(y)}")
# print(f"x-y={float(x)-float(y)}")


#逻辑运算符  and   or    not  返回bool值
#案例 输入一个整数，判断是否在10~20
num = input("请输入一个数：")
print(int(num)>=10 and int(num)<=20)
print(10<=int(num)<=20)

#案例 输入一个整数，判断是否不在10~20
print(int(num)>20 or int(num)<10)
print(not 10<=int(num)<=20)