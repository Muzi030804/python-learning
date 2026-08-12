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

# python

## 1—8：入门

### 快捷键

快速注释  Ctrl+/

快速复制一行 Ctrl+D

新建一行 Ctrl+Enter

列选择模式  Alt + Shift + Insert

跳到下一个匹配的符号	Tab	按Tab后光标会移动到}后
![image-20260807154238807](../assets/images/image-20260807154238807.png)

删除整行 Ctrl+Y

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



print(f"你的余额是：{money**:.1f**}")   #表示保留一位小数

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

  / 除法结果是小数  // 整除，结果是整数  %取余  **:幂指数：

```
10**3 = 10的3次方
```

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

判断一个元素是否存在于列表:  元素   (not)  in   列表      

返回结果为bool值,True表示存在(不存在),False表示不存在(存在)

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

```python
#列表一次可以存储多个数据
#定义:  列表名称 = [元素1,元素2,元素3...]
#列表可以存储不同类型的元素  可以同时存int float bool str等
#元素有序,可以重复,元素可以修改
#索引:        s[0],s[1],s[2],s[3]
#支持反向索引: s[-4],s[-3],s[-2],s[-1]   从-1

s = [12,33,22,34,"a"]
print(s[0])
print(s[-5])  #都是12

#修改
s[4] = "b"
print(s)

#删除
del s[4]
print(s)

#遍历
for item in s:
    print(item)
```

#### 列表的切片

```python
#切片:对操作的数据截取其中一部分       列表,字符串,元组都支持切片
#语法:  序列数据[开始索引:结束索引:步长]
#包含开始索引对应的元素,不包含结束索引对应的元素,开始索引默认为0,结束索引未指定默认为列表长度,步长默认为1
#索引正向,反向都可以
s = ["a","b","c","d","e","f"]

l = s[:5]   #['a', 'b', 'c', 'd', 'e']
print(l)
l = s[5:]   #['f']
print(l)
l = s[:]    #['a', 'b', 'c', 'd', 'e', 'f']
print(l)
l = s[0:4:2]    #['a', 'c']
print(l)
l = s[5:1:-1]   #['f', 'e', 'd', 'c']  开始索引大于结束索引时步长需为负,此时从后往前遍历
print(l)
l = s[1:1]  #[]    开始索引和结束索引指向同一个时为空
print(l)
l = s[-6:-1]    #['a', 'b', 'c', 'd', 'e']
print(l)
l = s[-1:-6]  #[]
print(l)
l = s[0:-5]  #['a']
print(l)
```

### 列表的常用方法

```python
# append()   在列表尾部加元素  s.appen(10000)
# insert()   在指定索引前,插入该元素  s.insert(0,92)
# remove()   移除列表中第一个匹配到的值  s.remove(75)
# pop()      删除列表中指定索引位置的元素(如果未指引,默认最后一个)  s.pop(2)/s.pop()
# sort()     对列表元素进行排序(列表元素的数据类型一致,才可以进行排序)  s.sort()
# reverse()  反转列表元素  s.reserve()
# sum()      求和         sum(s)
# len()      数组中多少元素    len(s)
# index()	 返回该元素的第一个索引  s.index(5)
s = [11, 2, 31, 4, -5, 15, 17, 28]
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28]
s.append(10)
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28, 10]
s.insert(1,10)
print(s)    #[11, 10, 2, 31, 4, -5, 15, 17, 28, 10]
s.remove(10)
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28, 10]
s.pop()
print(s)    #[11, 2, 31, 4, -5, 15, 17, 28]
s.sort()
print(s)    #[-5, 2, 4, 11, 15, 17, 28, 31]
s.reverse()
print(s)    #[31, 28, 17, 15, 11, 4, 2, -5]      
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list1.sort()
print(list1)#['A', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
```

```py
#案例:将输入的10个数字,存储到一个列表中,并排序,输出其中的最小值,最大值和平均值
list1 = []
for i in range(10):
    num = int(input("输入一个数字:"))
    list1.append(num)
print(list1)
list1.sort()
print(list1)
print(f"最小值为:{list1[0]}")
print(f"最大值为:{list1[9]}")
print(f"最大值为:{list1[-1]}")

s = 0
for i in list1:
    s += i
print(f"平均值为:{s/10}")
print(f"平均值为:{sum(list1)/len(list1)}")
```

合并两个列表中的元素,并对合并后的结果进行去重**(三种合并方式)**

### 解包:将列表这一类容器解开成一个一个独立的元素   

new_list = [*num_list1, *num_list2]

判断一个元素是否存在于列表:  元素   (not)  in   列表      

返回结果为bool值,True表示存在(不存在),False表示不存在(存在)

```python
num_list1 = [19,23,54,64,875,20,109,232,123,54]
num_list2 = [55,80,72,35,60,123,54,29,91]
# new_list = [*num_list1, *num_list2]    三种合并方式,推荐前两种
# new_list = num_list1 + num_list2
new_list = num_list1
for i in num_list2:
    num_list1.append(i)

print("合并后的列表为:", new_list)
l = []
for num in new_list:
    if num not in l:
        l.append(num)
print(f"去重后的数组为:{l}")
```

### 列表推导式

生成1~20的平方列表

```python
#方法一
 l = []
 for i in range(1,21):
     l.append(i**2)
 print(l)
#方法二:列表推导式    按照一定的规则快速生成一个列表  语法格式:   [要插入的值 for  i  in 序列/列表]
num_list = [i**2 for i in range(1,21)]
print(num_list)
```

从如下数字列表中提取所有偶数,并计算其平方,组成新的列表

```python
#方法一:
num_list = [19,23,54,64,97,20,109,232,123,43,26,55,72]
l = []
for num in num_list:
    if num % 2 == 0:
        l.append(num**2)
print(l)
#方法二:列表推导式   [要插入的值 for  i  in 序列/列表 if 条件]
new_list = [ i**2 for i in num_list if i % 2 == 0]
print(new_list)
```

### 字符串

#字符串是字符的容器,一个字符串可以放任意数量的字符    如:"Python"  'Python'  """Python"""
#特点:不可变(无法修改)    有序性    可迭代性(可以通过for循环遍历)
#字符串中的每一个字符元素都有其对应的下标,支持正向  反向索引
#字符串切片    语法: 序列对象[开始索引:结束索引:步长]

```python
s = "hello-world"
print(s[4])
print(s[-1])

# s[4] = "x"   报错,不支持修改
# print(s[4])

for i in s:
    print(i)

#切片
print(s[1:5])
print(s[-1:-5:-1])
```

#### 字符串常用方法

```python
#find()     查找子串,返回第一次出现的索引位置,找不到返回-1      s.find('Python')
#count()    统计子串在字符串中出现的次数      s.count('H')
#upper()    将字符串中所有字母转换为大写      s.upper()
#lower()    将字符串中所有字母转换为小写      s.lower()
#split()    将字符串按指定分隔符分割为列表     s.split(' ')			不传参数的 split() 会自动处理连续空白。
#strip()    去除字符串两端的空白字符或指定字符   s.trip()/strip('s')   默认空格
#replace()  将字符串的指定子串替换为新的子串    s.replace('H','C')
#startswith()  检查字符串是否以指定子串开头,返回bool值   s.startswith('P')
#endswith()     检查字符串是否以指定子串结尾,返回bool值   s.endswith('P')

print(s.find('hello')) #0
print(s.count('l'))  #3
up_str = s.upper()
print(up_str)       #HELLO-WORLD
low_str = s.lower()
print(low_str)      #hello-world
l = s.split('-')
print(l)            #['hello', 'world']
ss = s.strip('l')
print(ss)           #hello-world
ss = " hello-world "
print(ss)           # hello-world
print(ss.strip())   #hello-world   把空格去除了
sss = s.replace('l','e')
print(sss)          #heeeo-wored
print(s.startswith('h'))    #True
print(s.endswith('e'))      #False

print(s)   #hello-world   字符串不会变
```

案例:邮箱格式验证:用户输入一个邮箱,验证邮箱格式是否正确(包含一个@和至少一个.),如果正确就输出"邮箱格式正确",否则输出"邮箱格式错误"

```python
email = input("请输入您的邮箱:")
# 方法一:
if email.count("@") == 1 and email.count(".") >= 1 :
    print("邮箱格式正确")
else:
    print("邮箱格式错误")

#方法二:    in
if email.count("@") == 1 and "." in email:
    print("邮箱格式正确")
else:
    print("邮箱格式错误")

```

​    练习1：输入一个字符串, 判断该字符串是否是回文(两边对称)

```python
s = input("输入一个字符串:")
#方法一:   双指针
flag = True
light = 0
right = len(s) -1
while light<right:
    if s[light]!=s[right]:
        flag = False
        break
    light+=1
    right-=1
if flag:
    print("该字符串回文")
else:
    print("该字符串不回文")

#方法二: 直接反转比较
if s == s[::-1]:
    print("该字符串回文")
else:
    print("该字符串不回文")
#方法三:  类似双指针  
num = 0     #len(s)   直接获取长度
for char in s:
    if char != "":
        num+=1
print(f"字符串长度为:{num}")
flag = True
for i in range(num):
    if s[i] != s[len(s)-1-i]:
        flag = False
if flag:
    print("该字符串回文")
else:
    print("该字符串不回文")
```

练习2：将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容，遍历输出出来。

```python
s = []
for i in range(10):
    string = input("输入一个字符串:")
    s.append(string)      #s.append(string[::-1].upper())
    s[i] = s[i][::-1].upper()

for i in s:
    print(i)
```

### 元组

元组一旦创建不能修改
可以存储不同类型的元素
元素可以重复,有序,不可以修改,支持索引访问,切片
定义元组      元组名称 = (元素1,元素2...)
t1 = (1,5,6,9,6,4)
定义空元组	元组名称 = ()	t2 = ()
或者元组名称 = tuple()	t3 = tuple()
因为不能修改,所以只支持查询,统计操作
#count()  统计某元素出现的次数
#index()  查找某个元素在元组中的索引位置(第一次出现的位置)

```python
t1 = (1,5,6,9,6,4)
print(type(t1))     #<class 'tuple'>
print(t1[0])        #1
print(t1[-1])       #4

print(t1.count(6))  #2
print(t1.index(5))  #1

#切片
print(t1[1:4])  #(5, 6, 9)

#定义单个元素的元组   要在后面加逗号
t2 = (100)   #int
print(type(t2)) #<class 'int'>
t3 = (100,)     #tuple
print(type(t3))  #<class 'tuple'>
```

组包(Packing):将多个值合并到一个容器(元组或列表)中

解包(Unpacking):将容器(元组或列表)解开成独立的元素,分别赋值给多个变量

```python
#定义元组
t1 = (5,7,9,1)  #组包
t2 = 5,7,9,1    #组包
#基础解包
a,b,c,d = t1
print(a,b,c,d)  #5 7 9 1
# q,w,r = t1    #报错:too many values to unpack
# print(q,w,r)
# a,b,c,d,e = t1  #报错:not enough values to unpack
# print(a,b,c,d,e)
#(*)扩展解包   元组解包时, * 表示收集剩下的所有元素,生成列表
x,*y,z = t2    #x为5,y为[7,9],z为1
s, *o = t2      #s为5,o为[7,9,1]
*o, e = t2     #o为[5,7,9],e为1
```

案例1:现有两个变量,分别为a = 10, b = 20 现需要将两个变量值交换,然后输出

```python
a = 10
b = 20
# t = a,b
# b,a = t
#这两行可以简化为
a,b = b,a
print("b:",b)
print("a:",a)
```

案例2:现有三个变量,分别为a = 100, b = 200,c = 300, 现需要将三个变量值交换,将a,b,c的值分别赋给c,a,b然后输出

```python
a,b,c = 100,200,300
# t = a,b,c
# c,a,b = t
#简化为
c,a,b = a,b,c
print("c",c)
print("a",a)
print("b",b)
```

给定订单元组：

```
(
    ("A001", "键盘", 2, 199),
    ("A002", "鼠标", 3, 89),
    ("A003", "显示器", 1, 1299)
)
```

每条订单依次表示：订单号、商品名、数量、单价。遍历订单，输出每条订单的小计，最后输出全部订单总额。

```python
#解包,不依赖索引
orders = (
    ("A001", "键盘", 2, 199),
    ("A002", "鼠标", 3, 89),
    ("A003", "显示器", 1, 1299)
)

total = 0

for order_id, product_name, quantity, unit_price in orders:
    subtotal = quantity * unit_price
    print(f"{order_id}\t{product_name}\t小计：{subtotal}")
    total += subtotal

print(f"订单总额：{total}")
```

根据学生成绩单完成以下需求:

1.计算各个学生的总分,各科平均分,然后一并输出

2.统计各科成绩的最低分  最高分  平均分,并输出

3.查找成绩优秀(平均分>90)的学生,并输出

students =(
    ("S001","a",85,92,78),
    ("S002","b",92,88,95),
    ("S003","c",78,85,82),
    ("S004","d",88,79,91),
    ("S005","e",95,96,89),
    ("S006","f",76,82,77),
    ("S007","g",89,91,94),
    ("S008","h",75,69,82),
    ("S009","i",86,89,98),
    ("S010","j",66,59,72),
)

```python
# 1.计算各个学生的总分,各科平均分,然后一并输出
#方法一
# for stu in students:
#     print(f"学生{stu[1]}的总分为:{stu[2]+stu[3]+stu[4]}")
#     print(f"学生{stu[1]}的平均分为:{(stu[2]+stu[3]+stu[4])/3:.1f}")
#方法二
for uid,name,chinese_score,math_score,english_score in students:
    total = chinese_score + math_score + english_score
    avg = total /3
    print(f"学生{name}的总分为:{total}")
    print(f"学生{name}的平均分为:{avg}")
# 2.统计各科成绩的最低分  最高分  平均分,并输出

#获取成绩列表  简介写法  可以使用max(),min(),sum()
chinese_scores = [s[2] for s in students]
math_scores = [s[3] for s in students]
english_scores = [s[4] for s in students]
print(f"语文最低分为:{min(chinese_scores)},最高分为:{max(chinese_scores)},平均分为:{sum(chinese_scores)/len(chinese_scores):.1f}")
print(f"数学最低分为:{min(math_scores)},最高分为:{max(math_scores)},平均分为:{sum(math_scores)/len(math_scores):.1f}")
print(f"英语最低分为:{min(english_scores)},最高分为:{max(english_scores)},平均分为:{sum(english_scores)/len(english_scores):.1f}")
# chinese_min = students[0][2]
# chinese_max = students[0][2]
# math_min = students[0][3]
# math_max = students[0][3]
# english_min = students[0][4]
# english_max = students[0][4]
# chinese_sum =0
# math_sum = 0
# english_sum = 0
# for stu in students:
#     if stu[2] < chinese_min:
#         chinese_min = stu[2]
#     if stu[3] < math_min:
#         math_min = stu[3]
#     if stu[4] < english_min:
#         english_min = stu[4]
#     if stu[2] > chinese_max:
#         chinese_max = stu[2]
#     if stu[3] > math_max:
#         math_max = stu[3]
#     if stu[4] > english_max:
#         english_max = stu[4]
#     chinese_sum+=stu[2]
#     math_sum+=stu[3]
#     english_sum+=stu[4]
# chinese_avg = chinese_sum / len(students)
# math_avg = math_sum / len(students)
# english_avg = english_sum / len(students)
# print(f"语文最低分为:{chinese_min},最高分为:{chinese_max},平均分为:{chinese_avg:.1f}")
# print(f"数学最低分为:{math_min},最高分为:{math_max},平均分为:{math_avg:.1f}")
# print(f"英语最低分为:{english_min},最高分为:{english_max},平均分为:{english_avg:.1f}")
# 3.查找成绩优秀(平均分>90)的学生,并输出
#写法一:
# for stu in students:
#     if (stu[2]+stu[3]+stu[4])/3 > 90:
#         print(f"{stu[1]}的成绩优秀,学号为:{stu[0]},平均分为:{(stu[2]+stu[3]+stu[4])/3:.1f}")
#写法二:
for uid,name,chinese_score,math_score,english_score in students:
    total = chinese_score + math_score + english_score
    avg = total /3
    if avg > 90:
        print(f"学号:{uid},姓名:{name},平均分:{avg:.1f}")
```

### 集合

集合(set)是**无序,不可重复(重复元素自动去重),可修改**的数据容器

```python
#定义
s1 = {"c","d","e"}
#空集合
s2 = set()      #不可以使用{},{}表示的是空字典,由于集合是无序的,因此不支持小标索引
```

#### 常用方法

| add()        | 添加元素到集合                                      | s.add('t')          |
| ------------ | --------------------------------------------------- | ------------------- |
| remove()     | 移除集合中指定元素(不存在则报错)                    | s.remove('t')       |
| pop()        | 随机删除集合中的元素并返回                          | e = s.pop()         |
| clear()      | 清空集合                                            | s.clear()           |
| difference() | 求两个集合的差集(第一个集合有,第二个集合没有的元素) | s1.difference(s2)   |
| union()      | 求两个集合的并集                                    | s1.union(s2)        |
| intersection | 求两个集合的交集                                    | s1.intersection(s2) |

```python
s1 = {100,200,300,400,500,600,700,800}
s1.add(1200)
print(s1)       #{800, 100, 200, 300, 400, 1200, 500, 600, 700}

s1.remove(200)
print(s1)       #{800, 100, 300, 400, 1200, 500, 600, 700}

e = s1.pop()
print(e)        #800
print(s1)       #{100, 300, 400, 1200, 500, 600, 700}

s1.clear()
print(s1)       #set()

s2 = {"A","B","C","D","E","X","Y"}
s3 = {"C","E","Y","Z"}
print(s2.difference(s3))        #{'B', 'D', 'A', 'X'}
print(s2.union(s3))             #{'Y', 'D', 'Z', 'A', 'X', 'B', 'E', 'C'}
print(s2.intersection(s3))      #{'E', 'Y', 'C'}
```

#### 集合推导式     快速构建集合,语法:    {要往集合中添加的元素   for s in set if 条件}

&表示交集    |表示并集	-表示差集

案例:
选修足球学生名单

football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}

选修篮球学生名单

basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}

选修法语学生名单

french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}

选修艺术学生名单

art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

1.找出同时选择了法语和艺术的学生

2.找出同时选择所有四门课程的学生
3.找出选择了足球,但是没有选择篮球的学生
4.统计每一个学生的课程数量

```python
# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}
#1.找出同时选择了法语和艺术的学生  &也可以表示交集&
print(f"同时选择了法语和艺术的学生:{french_set.intersection(art_set)}")
print(f"同时选择了法语和艺术的学生:{french_set & art_set}")

#2.找出同时选择所有四门课程的学生
print(f"同时选择所有四门课程的学生:{football_set.intersection(basketball_set).intersection(french_set).intersection(art_set)}")
print(f"同时选择所有四门课程的学生:{football_set & basketball_set & french_set & art_set}")

#3.找出选择了足球,但是没有选择篮球的学生  -(减号)也可以表示差集
print(f"找出选择了足球,但是没有选择篮球的学生:{football_set.difference(basketball_set)}")
print(f"找出选择了足球,但是没有选择篮球的学生:{football_set - basketball_set}")
#还可以通过集合推导式     快速构建集合,语法:    {要往集合中添加的元素   for s in set if 条件}
s1 = {s for s in football_set if s not in basketball_set}
print(f"找出选择了足球,但是没有选择篮球的学生:{s1}")

#4.统计每一个学生的课程数量
# name = football_set.union(basketball_set).union(art_set).union(french_set)
#也可以用  |表示并集
name = football_set | basketball_set | french_set | art_set
#因为集合中元素不能重复,因此可以用列表   解包操作
all_list = [*football_set, *basketball_set, *french_set, *art_set]
for n in name:
    print(f"{n}选择的课程数量为:{all_list.count(n)}")
#笨方法
# for n in name:
#     num = 0
#     if n in football_set:
#         num += 1
#     if n in basketball_set:
#         num += 1
#     if n in art_set:
#         num += 1
#     if n in french_set:
#         num += 1
#     print(f"{n}选择的课程数量为:{num}")
```

### 字典

字典(dict),里面存储的是键值对(key: value)类型的数据,可以根据键(key)找到对应的值(value)
特点:以键值对(key: value)形式存储   键(key)不能重复,可修改
注意:字典(dict)中的value可以是任何类型的数据,而key不能为可变类型(如:列表,集合,字典),不可变类型有int,float,string,tuple

```python
#定义:    字典名称 = {key: value,key: value,key: value...}
#key不能重复,如果重复不会报错,但后面的会把前面的覆盖
dict1 = {"a": 1, "b": 2, "c": 3, "a": 4}
print(dict1)        #{'a': 4, 'b': 2, 'c': 3}
print(type(dict1))  #<class 'dict'>
dict1 = {(1,2): 1, 100: 2, 3.14: 3, "a": 4}
print(dict1)        #{(1, 2): 1, 100: 2, 3.14: 3, 'a': 4}    不可变类型有int,float,string,tuple
# dict1 = {[1,2]: 1, 100: 2, 3.14: 3, "a": 4}   报错:cannot use 'list' as a dict key  因为list是可变类型

#定义空字典  字典名称 = {}   字典名称 = dict()
dict2 = {}
dict3 = dict()
print(dict2)        #{}
print(type(dict2))  #<class 'dict'>
print(dict3)        #{}
print(type(dict3))  #<class 'dict'>

#根据key获取value
print(dict1["a"])      #4
dict1["a"] = 100
print(dict1["a"])       #100   可以修改
```

#### 常用操作

| 类型 |          操作           |                    含义                    |         样例         |
| :--: | :---------------------: | :----------------------------------------: | :------------------: |
| 添加 |  字典名称[key] = value  |           往指定字典中添加键值对           |   dict1["a"] = 10    |
| 删除 |    字典名称.pop(key)    | 删除字典中指定的key,并返回该key对应的value | num = dict1.pop("a") |
| 删除 |   del   字典名称[key]   |              删除指定的键值对              |  del    dict1["a"]   |
| 修改 | 字典名称[key]  =  value |           修改指定的key对应的值            |   dict1["a"] = 100   |
| 查询 |      字典名称[key]      |              根据key获取value              |      dict1["a"]      |
| 查询 |    字典名称.get(key)    |              根据key获取value              |    dict1.get("a")    |
| 查询 |     字典名称.keys()     |               获取所有的key                |     dict1.keys()     |
| 查询 |    字典名称.values()    |              获取所有的value               |    dict1.values()    |
| 查询 |    字典名称.items()     |         获取所有的key-value键值对          |    dict1.items()     |

```python
dict1 = {"a": 1, "b": 2, "c": 3, "d": 4}
#查询
print(dict1.get("c"))       #3
print(dict1["c"])           #3

print(dict1.keys())         #dict_keys(['a', 'b', 'c', 'd'])
print(dict1.values())       #dict_values([1, 2, 3, 4])
print(dict1.items())        #dict_items([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

#删除
num = dict1.pop("c")        #有返回值
print(num)                  #3
print(dict1)                #{'a': 1, 'b': 2, 'd': 4}

del dict1["d"]              #无返回值
print(dict1)                #{'a': 1, 'b': 2}

#遍历
for k in dict1.keys():
    print(f"{k}: {dict1[k]}")       #a: 1  (中间换行) b: 2
for item in dict1.items():          #item是元组('a', 1)    ('b', 2)
    print(f"{item[0]}: {item[1]}")  #a: 1  (中间换行) b: 2
for k, v in dict1.items():          #解包然后遍历
    print(f"{k}: {v}")              #a: 1  (中间换行) b: 2
```

案例
开发购物车管理系统,实现商品信息的增删改查功能,系统使用字典结构存储商品数据,通过控制台菜单与用户交互,具体功能如下
1.添加购物车:用户根据提示录入商品名称以及该商品的价格,数量保存该商品信息到购物车
2.修改购物车:要求用户输入要修改的购物车商品名称,然后再提示输入该商品的价格,数量,输入完成后修改该商品信息
3.删除购物车:要求用户输入要删除的购物车名称,根据名称删除购物车中的商品
4.查询购物车:将购物车中的商品信息展示除了,格式为:"商品名称: xxx,商品价格: xxx,商品数量: xxx"
5.退出购物车

```python
#购物车数据
#shopping_cart = {"商品1":{"price":200,"num":2},"商品2":{"price":100,"num":1}...}
shopping_cart = {}
#控制台菜单
print("##########购物车系统##########")
print("#        1.添加购物车        #")
print("#        2.修改购物车        #")
print("#        3.删除购物车        #")
print("#        4.查询购物车        #")
print("#        5.退出购物车        #")
print("############################")
valid_choose = ["1", "2", "3", "4", "5"]

while True:
    choose = input("请选择要执行的操作(1~5):")
    if choose not in valid_choose:
        choose = input("输入无效,请输入1~5:")
        continue
    match choose:
        #添加购物车功能
        case "1":
            name = input("请输入要录入的商品:")
            if name not in shopping_cart.keys():
                price = float(input("请输入该商品价格:"))
                num = int(input("请输入购买数量:"))
                shopping_cart[name] = {"price": price, "num": num}
            else:
                print("该商品已存在")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        #修改购物车
        case "2":
            name = input("请输入要修改的商品:")
            if name in shopping_cart.keys():
                price = float(input("请输入该商品价格:"))
                num = int(input("请输入购买数量:"))
                shopping_cart[name] = {"price": price, "num": num}
            else:
                print("该商品不存在")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        #删除购物车
        case "3":
            name = input("请输入要删除的商品:")
            if name in shopping_cart.keys():
                del shopping_cart[name]
                print(f"{name}已删除")
                print(f"当前购物车:{shopping_cart}")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        case "4":
            #查询购物车
            for name,msg in shopping_cart.items():
                print(f"商品名称:{name},商品价格:{msg.get("price")},商品数量为:{msg.get("num")}")
            choose = input("请选择要执行的操作(1~5):")
            if choose not in valid_choose:
                choose = input("输入无效,请输入1~5:")
        case "5":
            print("已退出系统")
            break
```

### 数据容器总结

![image-20260806093126383](../assets/images/image-20260806093126383.png)

开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
5. 列出所有学生：遍历所有学生信息并输出。
6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
7. 退出系统。

```python
students_msg = {}
menu = """
########################################[菜单]##############################################################
#  1. 添加学生信息  2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5. 列出所有学生  6. 统计班级成绩  7. 退出系统     #
###########################################################################################################

请选择要执行的操作(1~7):
"""
# 修改1：不在菜单循环外长期保存统计列表。
# 统计功能每次都从 students_msg 重新取数，避免修改、删除学生后仍保留旧成绩。

while True:
    choose = input(menu)

    match choose:
        case "1":
            # 1. 添加学生信息
            # 修改2：去除姓名首尾空格，并拒绝空姓名。
            name = input("请输入学生姓名:").strip()
            if name == "":
                print("学生姓名不能为空")
                continue
            if name in students_msg:
                print("该学生已存在")
            else:
                # 修改3：验证三科成绩，只接受 0~100 的整数。
                score_values = []
                for subject in ("语文", "数学", "英语"):
                    while True:
                        score_text = input(f"请输入{subject}成绩:")
                        if score_text.isdigit() and 0 <= int(score_text) <= 100:
                            score_values.append(int(score_text))
                            break
                        print("成绩无效，请输入0~100的整数")

                chinese_score, math_score, english_score = score_values
                students_msg[name] = {"chinese_score": chinese_score, "math_score": math_score, "english_score": english_score}
                print(f"学生{name}添加完成")

        case "2":
            # 2. 修改学生信息
            name = input("请输入要修改的学生姓名:").strip()
            if name == "":
                print("学生姓名不能为空")
                continue
            if name not in students_msg:
                print("该学生不存在")
            else:
                # 修改4：修改成绩时使用与添加功能相同的验证规则。
                score_values = []
                for subject in ("语文", "数学", "英语"):
                    while True:
                        score_text = input(f"请输入{subject}成绩:")
                        if score_text.isdigit() and 0 <= int(score_text) <= 100:
                            score_values.append(int(score_text))
                            break
                        print("成绩无效，请输入0~100的整数")

                chinese_score, math_score, english_score = score_values
                students_msg[name] = {"chinese_score": chinese_score, "math_score": math_score, "english_score": english_score}
                print(f"学生{name}修改完成")
        case "3":
            # 3. 删除学生信息
            name = input("请输入要删除的学生姓名:").strip()
            if name == "":
                print("学生姓名不能为空")
                continue
            if name not in students_msg:
                print("该学生不存在")
            else:
                del students_msg[name]
                print(f"学生{name}信息删除成功")
        case "4":
            # 4. 查询学生信息
            name = input("请输入要查询的学生姓名:").strip()
            if name == "":
                print("学生姓名不能为空")
                continue
            if name not in students_msg:
                print("该学生不存在")
            else:
                # 修改5：使用中文字段展示查询结果，不直接暴露内部键名。
                score = students_msg[name]
                print(
                    f"姓名:{name}, "
                    f"语文:{score['chinese_score']}, "
                    f"数学:{score['math_score']}, "
                    f"英语:{score['english_score']}"
                )
        case "5":
            # 5. 列出所有学生
            if not students_msg:
                print("当前没有学生信息")
            else:
                print(f"{'姓名':<8}{'语文':<6}{'数学':<6}{'英语':<6}")

                # 修改6：只使用一层 items() 遍历，保证姓名与成绩来自同一条记录。
                for name, score in students_msg.items():
                    print(
                        f"{name:<10}"
                        f"{score['chinese_score']:<8}"
                        f"{score['math_score']:<8}"
                        f"{score['english_score']:<8}"
                    )

        case "6":
            # 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名
            # 修改7：空字典不能调用 max() 和 min()，先进行空数据判断。
            if not students_msg:
                print("当前没有学生，无法统计成绩")
                continue

            # 修改8：每次统计时从当前字典重新生成列表，不保留历史数据。
            chinese_scores = [score["chinese_score"] for score in students_msg.values()]
            math_scores = [score["math_score"] for score in students_msg.values()]
            english_scores = [score["english_score"] for score in students_msg.values()]

            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            math_max = max(math_scores)
            math_min = min(math_scores)
            english_max = max(english_scores)
            english_min = min(english_scores)

            # 修改9：找出所有并列最高分和最低分的学生，不再只返回第一人。
            chinese_max_names = [name for name, score in students_msg.items() if score["chinese_score"] == chinese_max]
            chinese_min_names = [name for name, score in students_msg.items() if score["chinese_score"] == chinese_min]
            math_max_names = [name for name, score in students_msg.items() if score["math_score"] == math_max]
            math_min_names = [name for name, score in students_msg.items() if score["math_score"] == math_min]
            english_max_names = [name for name, score in students_msg.items() if score["english_score"] == english_max]
            english_min_names = [name for name, score in students_msg.items() if score["english_score"] == english_min]

            print(
                f"语文最高分:{chinese_max},姓名:{chinese_max_names}, "
                f"最低分:{chinese_min},姓名:{chinese_min_names}, "
                f"平均分:{sum(chinese_scores) / len(chinese_scores):.1f}"
            )
            print(
                f"数学最高分:{math_max},姓名:{math_max_names}, "
                f"最低分:{math_min},姓名:{math_min_names}, "
                f"平均分:{sum(math_scores) / len(math_scores):.1f}"
            )
            print(
                f"英语最高分:{english_max},姓名:{english_max_names}, "
                f"最低分:{english_min},姓名:{english_min_names}, "
                f"平均分:{sum(english_scores) / len(english_scores):.1f}"
            )
        case "7":
            # 7. 退出系统
            print("系统已退出")
            break

        # 修改10：为菜单增加默认分支，输入其他内容时给出明确提示。
        case _:
            print("输入无效，请输入1~7")
```

## 57—76：函数、模块、类型注解

### 函数定义与调用

```python
#def 函数名(参数列表):
#   函数体
#   ......
#   return 返回值          (可以没有返回值)

#调用函数       先定义再调用
#函数名(参数)

def out_line():
    print('--------------')

out_line()
```

### 参数与返回值

返回值可以有多个,会封装到元组中,可以用解包来分别获取

```python
#计算圆的面积
def circle_area(radius):
    return 3.14 * radius**2

c_area = circle_area(5)
print(c_area)

#计算长方形的面积
def rectangle(width, height):   #形参:函数定义时括号里的参数,只能在函数内使用(局部变量)
    return width * height

r_area = rectangle(5, 6)    #实参:函数在调用时输入的参数
print(r_area)

#计算圆的面积和周长
def circle_area_length(radius): #如果返回值有多个,多个返回值之间逗号分隔
    return round(3.14 * radius**2,1),round(2*3.14*radius,1)         #round(a,b):  让a保留b位小数
circle_area_len = circle_area_length(5)
print(circle_area_len)      #(78.5, 31.4)  多个返回值会封装到元组
print(type(circle_area_len))    #<class 'tuple'>

#解包
area, length = circle_area_length(5)
print(area)         #78.5
print(length)       #31.4
```

#### 函数的说明文档

函数的说明文档(Docstring)是写在函数开头,用三个引号包裹的字符串,用于解释函数的功能  参数  返回值等信息,方便调用者清楚函数的具体作用和细节

```python
def circle_area(radius):
    """
    该函数用于根据圆的半径,计算圆的面积和周长
    :param radius: 圆的半径
    :return: 圆的面积,圆的周长
    """
    return 3.14 * radius * radius,2*3.14*radius

a = circle_area(5)
print(a)
```

将光标放在调用的函数上就会出现说明文档

![image-20260807110911831](../assets/images/image-20260807110911831.png)

#### 函数的嵌套调用

嵌套调用值得是在一个函数中,又调用了另外一个函数
函数调用遵循栈结构,先进后出

```python
def function_a():
    print("function_a:first")
    function_b()
    print("function_a:last")
def function_b():
    print("function_b:first")
    function_c()
    print("function_b:last")

def function_c():
    print("function_c")

function_a()
#运行结果:
# function_a:first
# function_b:first
# function_c
# function_b:last
# function_a:last
```

### 变量作用域

全局变量:函数之外,整个文件中都可以使用,通常定义在文件顶部
局部变量:函数内部,只能在函数内部使用

```python
num = 100
def circle_area(radius):
    pi = 3.14
    area = pi * radius * radius
    num = 1000              #这是局部变量num,和全局变量num不是同一个num
    print("num:",num)
    return area
print(circle_area(10))		#num: 1000	314.0
print("num:",num)           #num: 100   这是全局变量num
```

#### global关键字

作用是在函数中要使用全局变量,使得可以在函数内部修改全局变量的值

注意事项:

不过尽量避免在函数中使用全局变量,因为会使代码难以维护

考虑使用函数参数和返回值来传递数据,而不是依赖全局变量

global主要用在程序的状态,配置,计数器等场景

```python
num = 1
def fun1():
    global num          #声明  使用全局变量num
    num = 100
    print("num:",num)

fun1()                  #num: 100
print("num:",num)       #num: 100
```

### 参数进阶

#### 传参方式

传参方式:在调用函数时,传递实参的方式
1.位置参数:调用时根据函数定义时的位置来传递参数    要求调用函数时参数顺序与定义函数时参数顺序完全一致

优点:简洁
缺点:可读性差 易出错 维护难

场景:参数少(不超过3个),且顺序自然

2.关键字参数:调用函数时以函数定义时形参名称作为关键字,以"键=值"的形式来传递(不要求顺序)

优点:可读性强 易维护和扩展
缺点:代码繁琐

场景:参数较多,或易混淆的场景

```python
def reg_stu(name,age,gender,city):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}

#位置参数
stu = reg_stu("小王",23,"男","重庆")
print(stu)
#关键字参数
stu = reg_stu(name="张三",age=18,gender="男",city="北京")
print(stu)
#与顺序无关
stu2 = reg_stu(gender="男",name="李四",city="上海",age=22)
print(stu2)
#如果位置参数与关键字参数混用,关键字参数必须在位置参数之后(关键字参数之间,没有顺序要求)
stu3 = reg_stu("王五",25,city="上海",gender="男")
print(stu3)
```

#### 默认参数

默认参数也称为缺省参数,用于在定义函数时,为参数提供默认值,调用函数时,可以不传递有默认值的参数

```python
def reg_stu(name,age,gender="男",city='北京'): #默认参数必须放在没有默认值的参数列表的后面,一个函数在定义时可以设置多个默认参数
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name":name,"age":age,"gender":gender,"city":city}
#函数调用时,如果默认参数传递了值,则会修改默认的参数值,如果没有传递该参数,则直接使用默认值
stu = reg_stu("张三",18)
print(stu)
stu = reg_stu("李四",22,"男","南京")
print(stu)
stu = reg_stu("王五",24,city="南京")
print(stu)
```

#### 不定长参数

不定长参数也叫可变参数,用于函数定义及调用时参数个数不确定(0个或多个)的场景()
类型:     位置传递   ,  关键字传递

不定长参数-位置传递(\*args)  传递的所有匹配的未知参数都会被args变量收集,这些参数会合并封装为一个元组,args是元组类型(注意并不会封装关键字参数)
\*args只是约定俗成的变量名,并不是关键字,可以使用任何合法的变量名(如\*data)

```python
def calc_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data,1)
data = calc_data(10, 20, 30, 40)
print(data)
data = calc_data(100, 200, 300, 400)
print(data)
```

不定长参数-关键字传递(\*\*kwargs)      参数是以"键=值"形式传递的关键字参数,这些"键=值"参数都会被kwargs接受,并合并为一个字典类型
\**kwargs只是约定俗成的变量名,并不是关键字,可以使用任何合法的变量名(如**options)

```python
def calc_data(*args,**kwargs):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args)/len(args)

    if kwargs.get('round') is not None:
        avg_data = round(avg_data,kwargs.get('round'))

    if kwargs.get('print'):
        print(min_data,max_data,avg_data)

    return min_data,max_data,avg_data

data = calc_data(100,200,301,round=2,print=True)  #100 301 200.33 round作用是几位小数 print表示是否打印
print(data)     #(100, 301, 200.33)

data = calc_data(33,32,13,45,35,67)     #无print,因为不满足kwargs.get('print') == True
print(data)     #(13, 67, 37.5)
```

### 函数作为参数

普通参数:int,bool,str,list,tuple,set,dict等
特殊参数:函数

```python
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def calculate(x,y,oper):        #oper是函数
    return  oper(x,y)           #函数调用语法

result = calculate(2,3,add)
print(result)
result = calculate(2,3,subtract)
print(result)
```

### lambda表达式(匿名函数)

匿名函数指的是没有名称的函数,需要通过lambda表达式来声明函数,可以简化简单函数的编写(单行表达式)
注意:函数逻辑比较简单(单行表达式)且只在一个地方使用时,可以考虑使用匿名函数,简化书写(通常作为高阶函数的参数使用)
注意:匿名函数中可以返回结果,也可以不返回结果,返回结果是不需要写return,表达式的运行结果就是要返回的结果

```python
#定义匿名列表
#lambda 参数列表 : 函数体              没有函数名

#需求1:打印一个分隔线
# def out_line():
#     print('------------')
out_line = lambda : print('-------------')  #匿名函数无法直接调用,所以需要赋值给变量,这个变量是一个函数
out_line()
#需求2:计算两数之和
# def add(x,y):
#     return x+y
add = lambda x,y: x+y          #lambda表达式会自动将结果返回,不需要写return
print(add(3,4))

#需求3:完成如下列表的排序操作,按照每一个元素的字符个数从小到大排序    匿名函数典型应用场景
data_list = ["C++","C","Python","Java","PHP","Go","JavaScript"]
data_list.sort(key=lambda item : len(item))         #sort函数中的参数key,表示按什么排序,key是一个函数
print(data_list)
```

### 类型注解

类型注解是python中的一种语法特性,用于明确表示变量,函数参数和返回值的数据类型,从而使代码更清晰,更安全,更易维护

```python
a = 100
b:int = 100
names : list[str] = ["A", "B", "C"]         
phone: set[str | int] = {"15915246633", "15915246634", "15915246635",12222555}
options:dict[str, int] = {"count":0,"total":0}
goods: tuple[str,int,int] = ("phone",2333,3)
```

### 综合练习

定义一个函数,用于根据传入的一批商品信息(商品名,价格,数量),优惠(优惠券,积分抵扣),运费信息计算订单的总金额
具体规则如下:
优惠券需要商品金额慢5000才可以使用,且优惠券金额不能超过商品总价
积分抵扣需要商品总金额满5000才可以使用,100 积分抵扣1元(且抵扣金额部门超过商品总价,积分只能整百抵扣)

```python
def clac_order_price(*args: tuple[str,float,int],coupon:int =0,score:int=0,freight=0) -> float | int:
    """

    :param args: 物品信息(商品名,价格,数量)
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param freight: 运费
    :return: 订单总金额
    """
    #商品金额
    total_price = [goods[1]*goods[2] for goods in args]
    total_cost = sum(total_price)

    #扣减优惠券
    if coupon > total_cost:
        coupon = total_cost

    total_cost = total_cost - coupon

    #扣减积分抵扣
    discount = score//100
    if score//100 > total_cost:
        discount = total_cost

    total_cost = total_cost - discount

    #添加运费
    total_cost = total_cost + freight

    return total_cost
print(clac_order_price(('phone',2000,3),('pad',1000,2),coupon=200,score=2000,freight=500))
print(clac_order_price(('phone',2000,1),('pad',1000,2),freight=100))
```

### 模块

Python模块(module):一个.py文件就是一个模块,模块是Python程序的基本组织单位.在模块中可以定义变量,函数,类,以及可执行的代码

#### 模块导入

|                导入形式                |                代码样例                 |   调用方式    |        调用方式        |
| :------------------------------------: | :-------------------------------------: | :-----------: | :--------------------: |
|             import  模块名             |            import  random,os            | 模块名.功能名 | random.randint(10,100) |
|        import  模块名  as  别名        |         import  random  as  rd          |  别名.功能名  |   rd.randint(10,100)   |
|      from  模块名  import  功能名      |  from  random  import  randint,choice   |    功能名     |    randint(10,100)     |
| from  模块名  import  功能名  as  别名 | from  random  import  randint  as  rint |     别名      |      rint(10,100)      |
|        from  模块名  import  *         |         from  random  import  *         |    功能名     |    randint(10,100)     |

```python
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
```

#### 自定义模块

每一个Python文件都可以作为一个模块,模块的名字就是文件的名字

_ _ name _ _

_ _ all _ _   :是一个模块级别的特殊变量,用与指定  from  模块名  import  *  时会导入哪些功能

my_func.py:

```python
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
print(__name__)     #__main__
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
```

main.py:

```python
#导入模块
import my_func      #直接导入会将 log_separator1() log_separator2() log_separator3() log_separator4()也输出,所以需要__name__判断

#使用模块中的功能
print(my_func.PI)
my_func.log_separator1()
my_func.log_separator2()
my_func.log_separator3()
my_func.log_separator4()

#导入自定义模块中的功能
from my_func import log_separator1,PI
print(PI)

from my_func import *
print(PI)
log_separator1()
# log_separator2() 会报错 因为__all__中没有 log_separator2()
```

### 包

包:本质就是一个文件夹,该文件夹中可以包含若干Python模块(.py文件),文件夹下还包含了一个_ _ init _ _.py
作用:模块文件较多时,用来管理多个模块(包的本质也是模块)

#### 导入方式

![image-20260810170246229](../assets/images/image-20260810170246229.png)

utils:

​	_ _ init _ _.py:

```python
#描述包信息
__version__ = "1.0.0"
__author__ = "me"
__all__ = ['my_func','my_var']
```

​	my_func.py:

```python
def log_separator1():
    print('-'*30)

def log_separator2():
    print('+'*30)

def log_separator3():
    print('#'*30)

def log_separator4():
    print('*'*30)
```

​	my_var.py:

```python
PI = 3.1415926
```

10_包.py:

```python
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
```

注意:若utils和10_包.py不在相同目录下,则导入需要使用绝对路径,假设utils在module_01文件夹中,则导入应为:from  module_01.utils......

## 77—87：面向对象和异常

### 面向对象基础

#### 类与对象

定义类    语法如下:          (不推荐以下动态的为对象添加属性)
class 类名:
    pass

创建对象
对象名 = 类名()
对象名.属性名1 = 属性值1
对象名.属性名2 = 属性值2
说明:类名的命名规范,遵循大驼峰命名法,每个单词的首字母大写,单词之间没有分隔符,比如:UserInfo,UserAccount

#说明:_ _ dict _ _是Python中用户自定义类实例的一个特殊属性,用于以字典形式存储对象的属性

```python
#定义类(不推荐动态的为对象添加属性)
class Car:
    pass
#创建对象
car1 = Car()
#动态的为对象添加属性(不推荐)
car1.brand = 'BMW'
car1.name = "X5"
car1.price = 500000
print(car1)                 #<__main__.Car object at 0x7f290da9b230>  后面是内存地址,每次运行都会发生变化
print(car1.__dict__)        #{'brand': 'BMW', 'name': 'X5', 'price': 500000}
```

定义类  语法如下:         (推荐)
class 类名:
    def _ _ init _ _(self,参数列表):
        self.属性名 = 参数值
        self.属性名 = 参数值
创建对象
对象名 = 类名(参数列表)

说明:定义在类的外面的称之为函数,定义在类中的函数称之为方法
_ _ init _ _:初始化方法,对象创建后会自动调用,主要用于设置对象的初始状态(设置对象属性)
self:方法的第一个参数,表示当前创建的实例对象

```python
#定义类
class Car:
    def __init__(self,c_brand,c_name,c_price):
        self.c_brand = c_brand
        self.c_name = c_name
        self.c_price = c_price
        print("初始化完毕")
#创建对象
c1 = Car("BMW",'X5',500000)     #初始化完毕
print(c1.__dict__)      #{'c_brand': 'BMW', 'c_name': 'X5', 'c_price': 500000}
print(c1.c_brand)       #BMW
print(c1)               #<__main__.Car object at 0x7f0cb009b230>
```

#### 实例方法

定义类
class 类名:
    def _ _ init _ _(self,参数列表):
        self.属性名 = 参数值
        self.属性名 = 参数值
    def 方法名(self,形参列表):
        ...
    def 方法名(self,形参列表):
        ...
创建对象
对象名 = 类名(参数列表)
对象名.方法名(实参)

```python
class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price


    def running(self):
        print(f"{self.brand} {self.name}正在行驶...")

    def total_price(self,discount,rate=0.1):
        """
        计算提车总费用
        :param discount: 折扣
        :param rate: 税率
        :return: 总费用
        """
        total_price = self.price*discount + self.price*rate
        return total_price

c1 = Car("BWM","X5",500000)
total1 = c1.total_price(0.9,0.2)
print(f"提车总价为:{total1:.0f}")       #提车总价为:550000
c1.running()                #BWM X5正在行驶...

c2 = Car("BWM","X5",500000)
total2 = c2.total_price(0.9)
print(f"提车总价为:{total2:.0f}")        #提车总价为:500000
```

#### 魔法方法

魔法方法是指Python中提供的以双下划线开头和结尾的特殊方法,用于定义类的特殊行为,比如:_ _ init _ _
魔法方法不需要手动调用,Python会在合适的时机自动调用

| 魔法方法                                          | 描述                                                         |
| ------------------------------------------------- | ------------------------------------------------------------ |
| _ _ init _ _                                      | 初始化方法                                                   |
| _ _ str _ _                                       | 字符串表示的方法                                             |
| _ _ eq _ _                                        | 比较两个对象是否相等(equal)                                  |
| _ _ lt _ _ , _ _ le _ _ , _ _ gt _ _ , _ _ ge _ _ | 支持比较两个对象的大小(less than),小于等于(less than or equal),大于(greater than),大于等于(greater than or equal) |

```python
class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def running(self):
        print(f"{self.brand} {self.name} 正在行驶...")
    def __str__(self):      #将print(对象)转化为字符串
        return f"{self.brand} {self.name} {self.price}"
    def __eq__(self, other):        #两个对象之间使用 == 会自动调用__eq__
        return self.brand == other.brand and self.name == other.name and self.price == other.price
    def __lt__(self, other):                ##两个对象之间使用 < 会自动调用__lt__,如果使用 > ,相当于取反,也可以调用
        return self.price < other.price

c1 = Car("BWM","X5",500000)
print(c1)       #<__main__.Car object at 0x7f3e39e9b230>    加入__str__后:    BWM X5 500000

c2 = Car("BWM","X5",500001)
print(c2)       #<__main__.Car object at 0x7f3e39e79f90>    加入__str__后:    BWM X5 500000

print(c1 == c2)     #False  如果直接比较两个对象,会基于对象的内存地址进行比较    加入__eq__后:   False(因为价格不一样)
print(c1 < c2)      #报错:TypeError: '<' not supported between instances of 'Car' and 'Car'   加入__lt__后:      True
```

#### 属性

实例属性:实例属性属于每个具体对象的属性,每个对象都是独立的(各个对象特有的数据)
类属性:雷属性是属于类本身的属性,所有实例共享的(所有对象共享的数据或配置)
说明:通过实例查找属性时,会先查找实例属性,实例属性不存在时,在查找类属性

```python
class Car:
    #类属性(所有实例对象共享)  通过 类名.属性 的方式操作
    wheel = 4       #轮胎数量
    tax_rate = 0.1  #购置税

    def __init__(self,brand,name,price):
        # 实例属性,通过 实例对象.属性 的方式操作
        self.brand = brand
        self.name = name
        self.price = price
        self.wheel = 2

    def running(self):
        print(f"{self.brand} {self.name}正在行驶...")

    def total_price(self, discount, rate=0.1):
        """
        计算提车总费用
        :param discount: 折扣
        :param rate: 税率
        :return: 总费用
        """
        total_price = self.price * discount + self.price * rate
        return total_price

c1 = Car("BWM", "X5", 500000)
print(Car.wheel)        #4
print(c1.wheel)         #2   通过实例查找属性时,会先查找实例属性,实例属性不存在时,在查找类属性
```

### 异常

异常(也称为bug)就是程序运行过程中出现的错误,它会中断程序的正常执行流程
作用:
保证数据,逻辑的正确性,避免程序执行混乱
在开发阶段,尽量发现更多的问题,尽早解决问题,保障程序正常执行

#出现异常有两种处理方案:
1.不做处理:整个程序因为一个bug,中断执行
2.捕获异常:按照我们自己的处理方式,处理完异常,程序继续执行(编写程序是,做好预案,出现异常,按预案处理)

try:
  可能出现异常的业务代码1
  可能出现异常的业务代码2
  ...
except [异常类型 as 变量名]           #[ ]表示可有可无
  出现异常时的原
[finally:
  不管是否出现异常,都会执行的代码]

```python
try:
    print("=============")
    # print(my_name)                  #运行错误,报错信息: name 'my_name' is not defined
    # print(1/0)                      #运行错误,报错信息: division by zero
    print("abc"[10])                    #程序运行出错,错误信息: string index out of range
    print("=============")
except NameError as e:              #捕获NameError异常
    print("运行错误,报错信息:",e)
except ZeroDivisionError as e:
    print("运行错误,报错信息:",e)
except Exception as e:              #捕获所有异常
    print("程序运行出错,错误信息:",e)
finally:                            #无论程序是否正常运行,finally代码块中的代码都会正常运行
    print("释放资源~")
```

#### 异常的传递

异常传递就是异常在函数调用中层层上报的过程,知道有人处理它,或者程序崩溃

```python
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
```

### 综合练习

采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车

```python
class Goods:
    def __init__(self,name,price,num):
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称:{self.name}  价格:{self.price}  商品数量:{self.num}"

    def update_price(self,price=None,num=None):
        if price is not None:
            self.price = price
        if num  is not None:
            self.num = num
class ShoppingCart:
    def __init__(self):
        self.shopping_cart_list = []

    #添加购物车
    def add_shopping_cart(self):
        name = input("输入添加的商品名称:")
        for good in self.shopping_cart_list:
            if good.name == name:
                print("该学生已存在")
                return
        price = float(input("输入价格:"))
        num = int(input("输入数量:"))
        self.shopping_cart_list.append(Goods(name,price,num))
        print("添加完成")

    #修改购物车
    def update_shopping_cart(self):
        name = input("输入修改的商品名称:")
        for good in self.shopping_cart_list:
            if good.name == name:
                price = float(input("输入价格:"))
                num = int(input("输入数量:"))
                good.update_price(price,num)
                print("修改完成")
                return
        print("该商品不存在")

    #删除购物车
    def delete_shopping_cart(self):
        name = input("输入删除的商品名称:")
        for good in self.shopping_cart_list:
            if good.name == name:
                self.shopping_cart_list.remove(good)
                print("删除完成")
                return
        print("该商品不存在")

    #查询购物车
    def show_shopping_cart(self):
        for good in self.shopping_cart_list:
            print(good)

    def run(self):

        while True:
            print()
            print("#########################################")
            print("1.添加信息  2.修改信息  3.删除信息  4.查询信息  5.退出系统 ")
            print("#########################################")
            choice = input("选择操作:")
            try:
                match choice:
                    case '1':
                        self.add_shopping_cart()
                    case '2':
                        self.update_shopping_cart()
                    case '3':
                        self.delete_shopping_cart()
                    case '4':
                        self.show_shopping_cart()
                    case '5':
                        print("退出成功")
                        return
                    case _:
                        print("请输入1~5")
            except Exception as e:
                print("程序错误,请重新输入")

if __name__ == '__main__':
    shopping_cart = ShoppingCart()
    shopping_cart.run()
```

# AI应用

## 88—99：大模型API

### 模型调用
