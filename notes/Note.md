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

新建一行 Ctrl+Enter

列选择模式  Alt + Shift + Insert

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



**转义字符\\'   \\"         \n（换行）   \t （缩进）   **制表符,\t 会把光标移动到下一个制表位

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

```python
#打印一个长度为m 宽度为n的长方形
m = int(input("长方形的长为:"))
n = int(input("长方形的宽为:"))
for i in range(n):
    for j in range(m):
        print("*",end=" ")  #表示这个输出语句以" "结束,默认是"\n"(换行)
    print()
```

print()默认换行

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

### 条件判断

#if判断格式   **python中是通过缩进来表示代码的层级关系**

if（条件）：             #注意冒号

​	操作

​	操作    #也是属于if代码块

操作    #不属于if代码块，独立运行

```python
#案例  完成登录功能（正确账号密码为1888/666888）
account = input("请输入您的账号：")
password = input("请输入您的密码：")
ok_account = "1888"
ok_password = "666888"

if account == ok_account and password == ok_password:
    print("登陆成功")
if account != ok_account or password != ok_password:
    print("登录失败")
```

#if...else...结构
if 条件：

​	操作

else:

​	操作



```python
#案例 根据输入的年份，判断是闰年还是平年  非整百且可以被4整除，整百必须被400整除才是闰年
year = input("请输入年份;")
if ( int(year) % 100 != 0 and int(year) % 4 == 0 ) or (int(year) % 100 ==0 and int(year) % 400 == 0 ):
    print("该年是闰年")
else:
    print("该年是平年")
```



简洁写法     **and优先级比or高**

```python
years = int(input("请输入年份："))
if years % 400 == 0 or years % 4 ==0 and years % 100 != 0:
    print("该年是闰年")
else:
    print("该年是平年")
```





#if...elif...else结构

if 条件1:

​	操作1

elif 条件2：

​	操作2

else：

​	操作3

#根据用户名 密码进行登录 用户名 密码分别为admin/666888,root/111111,zhangsan/123456,否则就提示用户名或密码错误

```python
name = input("输入用户名:")
password = input("输入密码:")
if name == "admin" and password == "666888":
    print("登陆成功")
elif name == "root" and password == "111111":
    print("登陆成功")
elif name == "zhangsan" and password == "123456":
    print("登陆成功")
else:
    print("用户名或密码错误")
```



### 模式匹配

match...case     匹配到会直接退出,不会继续往下

```python
day = int(input("今天是周几:"))
match day:
    case 1:
        print("今天是周一")
    case 2:
        print("今天是周二")
    case 3:
        print("今天是周三")
    case 4:
        print("今天是周四")
    case 5:
        print("今天是周五")
    case 6 | 7:
        print("今天是周末")
    **case _:**              #相当于else
        print("输入错误")
```

#实现一个计算器,可以实现+ - * / 运算,用户输入两个数以及运算符之后就可以进行运算

```python
a = float(input("a ="))
b = float(input("b ="))
s = input("s =")
match s:
    case "+":
        print(f"a+b={a} {s} {b} = {a+b}")
    case "-":
        print(f"a-b={a} {s} {b} = {a-b}")
    case "*":
        print(f"a*b={a} {s} {b} = {a*b}")
    case "/":
        if b == 0:
            print("除数不能为0")
        else:
            print(f"a/b={a} {s} {b} = {a/b}")

​	case _:
  	  print("运算符错误")
```



### 循环

while语法结构

while 条件:

​	循环语句1

​	循环语句2

​	...

else:                              #可有可无

​	条件为False,循环正常结束时运行       

```python
#案例计算1~100中的所有偶数和
n = 1
s = 0
while n <= 100:
    if n % 2 == 0:
        s += n
    n += 1
print(s)
```

for循环结构
for 元素 in 待处理数据集

​	循环体

else:

​	循环结束时执行的代码

```python
msg = "hello world"
for i in msg:
    print(i)
else:
    print("循环结束")
```

#### range语句

作用:生成指定规则的数字序列

用法1:range(end)      获取一个从0开始,到end结束的序列(不包含end)    range(5)->0,1,2,3,4

用法2:range(start,end)    获取一个从start开始,end结束的数字序列(不包含end)    range(2,8)->2,3,4,5,6,7

用法3:range(start,end,step)    获取一个从start开始,end结束的数字序列,step步长(不含end)    range(0,10,2)->0,2,4,6,8

```python
#计算100~500之间所有的3的倍数的数字之和
num =0
for i in range(100,501):
    if i % 3 == 0:
        num += i
print(num)
```

**while循环:用于某个条件满足时一直循环,循环次数未知,只知道开始和结束条件(关注循环的条件)**

**for循环:用于对已知的数据集进行遍历或已知次数的循环(关注的是遍历每一个元素)**

**break   只能用在循环中,表示跳出循环**

**continue 跳过本轮循环**

嵌套循环

```python
#打印一个长度为m 宽度为n的长方形
m = int(input("长方形的长为:"))
n = int(input("长方形的宽为:"))
for i in range(n):
    for j in range(m):
        print("*",end=" ")  #表示这个输出语句以" "结束,默认是"\n"(换行)
    print()
```

```python
#打印99乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end="\t")   #\t 会把光标移动到下一个制表位
    print()
```

```python
#登录
while True:
    account = input("输入账号:")
    password = input("输入密码:")

    if account == "" or password == "":
        print("用户名和密码不能为空,请重新输入")
        continue

    if account == "admin" and password == "666888" or account == "zhangsan" and password == "123456":
        print("登录成功")
        break
    print("用户名或密码错误,请重新输入")
```

## 36—56：数据容器

一种可以容纳多份数据的数据类型,容纳的每一份数据都称之为1个元素,每一个元素可以是任意类型的数据,如:字符串  数字  布尔等

列表(list)	字符串(str)	元组(tuple)	集合(set)	字典(dict)

### 列表--list
