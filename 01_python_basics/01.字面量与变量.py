# 字面量的写法

print(100)  #int
print(3.14)  #float
print(True)   #bool
print(False)   #bool
print("hello world")   #str
print("---------")   #str
print(None)   #空值 NoneType

#bool本质也是int t=1 f=0
print(True + 1)

#变量  python是动态类型语言，一个变量可以存储不同类型的数据，但不推荐
num = 100
print(num)
num = 101.1
print(num)
num = True
print(num)


#练习
num = 20.7 #基础播放量
add = 50   #每月新增
print("未来第一个月的播放量：",num + add)
print("未来第二个月的播放量：",num + add*2)  #未来两个月播放量

#支持一次性定义多个变量
num,add = 20.7,50


#p12
# 案例1 现有两个变量，分别为：a = 10，b = 20，现需要将两个变量值交换，然后输出

a = 10
b = 20
temp = a
a = b
b = temp
print(a)
print(b)

#案例2 现有三个变量，a = 100, b = 200, c = 300，先需要将三个变量值进行交换，将a，b，c的值分别赋给c,a,b,并输出

a,b,c = 100,200,300
d = a
a = b
b = c
c = d
print(a)
print(b)
print(c)

