

#输入：input，用法为：s = input（提示信息）  注意输入的数据一直都是字符串
name = input("请输入你的姓名：")
print(f"欢迎你：{name}")
age = input("请输入你的你年龄：")
print(f"你的年龄是：{age}")
print(type(age))   #输出为<class 'str'>

#案例银行卡中有10000元，现在去取款，根据输入的金额执行取钱操作，完成后展示余额
#步骤：1.输入密码  2.输入取款金额  3.计算余额并输出
balance = 10000
password = input("请输入您的密码：")
num = input("请输入取款金额：")
print(f"本次取款：{num}元，余额：{balance - int(num)}元")