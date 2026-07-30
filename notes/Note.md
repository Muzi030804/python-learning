每天要形成的习惯是：
看视频
  ↓
跟着写一遍
  ↓
关闭视频独立重写
  ↓
运行验证
  ↓
git diff检查
  ↓
git commit保存

## 1—8：环境安装与入门程序

### 快捷键

快速注释  Ctrl+/

快速复制一行 Ctrl+D

## 9—35：Python基础语法

基础数据类型：int,float,bool,str,NoneType

通过type()得到数据的类型，返回数据类型

通过isinstance(数据，类型) 判断数据是否是指定的类型，如果是：True，不是：False

### 字符串

字符串的三种定义：

s1 = "hello"
s2 = 'world'
s3 = """
hello
world
"""      可以换行，这个要按三次双引号

转义字符\\'   \\"           \t （缩进）       \n（换行）

s4 = 'It\\'s very good'    要用转义字符，不然会忽略最后的'

print("hello\nworld")
print("hello\tworld")

字符串拼接

s1 = "hello"
s2 = "world"

print("Hi" +","+ s1 + "," + s2 + "!")



+号只能拼接字符串与字符串，如果要拼接其他类型数据和字符串，用str（数据）

print("大家好，我是"+name + ",今年" + age + "岁,学习的专业是" + major)
print("大家好，我是"+name + ",今年" + str(age) + "岁,学习的专业是" + major)



#字符串格式化  %s:占位符    **f"内容{变量/表达式}"**（企业推荐）
#通过%占位符 的形式完成字符串与变量的快速拼接

print("大家好，我是%s，今年%s岁，学习的专业是%s"% (name, age, major))
print(f"大家好，我是{name},今年{age}岁，学习的专业是{major}")
a = 10
b = 20
print(f"a+b = {a+b}")



### 输入与输出

#输入：input，**用法为：s = input（提示信息）  注意输入的数据一直都是字符串**
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
print(f"本次取款：{num}元，余额：{balance - **int(num)**}元")



### 运算符

  / 除法结果是小数  // 整除，结果是整数  %取余  **幂指数：10**3 = 10的3次方

#案例  要求输入两个数x，y，分别输出x+y和x-y
x = input("请输入x：")
y = input("请输入y：")
print(f"x+y={float(x)+float(y)}")
print(f"x-y={float(x)-float(y)}") #可能损失精度



逻辑运算符

#逻辑运算符  and   or    not  返回bool值
#案例 输入一个整数，判断是否在10~20
num = input("请输入一个数：")
print(int(num)>=10 and int(num)<=20)
print(10<=int(num)<=20)

#案例 输入一个整数，判断是否不在10~20
print(int(num)>=20 or int(num)<=10)
