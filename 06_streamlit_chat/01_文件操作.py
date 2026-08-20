# 读文件
#
# 1.打开文件
# f = open("resources/静夜思.txt","r",encoding="utf-8")  #"r"表示读权限
#
# 2.读取文件内容
# content = f.read()      #读取所有内容
# print(content)
# content_list = f.readlines()
# print(content_list)         #['静夜思  [唐] 李白\n', '床前明月光,\n', '疑是地上霜.\n', '举头望明月,\n', '低头思故乡.']
# for line in content_list:
#     print(line.strip())     #因为每一行后面都有\n,所以用strip()
#
# #3.关闭文件
# f.close()


#写文件
#1.打开文件
# f = open("resources/春晓.txt","w",encoding="utf-8")   #没有这个文件,那么写操作时会自动创建
#
# #2.写文件
#
# f.write("春晓  [唐] 孟浩然\n")
# f.write("春眠不觉晓，\n")
# f.write("处处闻啼鸟。\n")
# f.write("夜来风雨声，\n")
# f.write("花落知多少。\n")
#
# #3.关闭文件
# f.close()



#释放资源
#方法一:使用try,finally
#1.打开文件
# f = open("resources/春晓.txt","w",encoding="utf-8")   #没有这个文件,那么写操作时会自动创建
#
# #2.写文件  #这样报错了也可以关闭文件
# try:
#     f.write("春晓  [唐] 孟浩然\n")
#     f.write("春眠不觉晓，\n")
#     f.write("处处闻啼鸟。\n")
#     i = 1/0
#     f.write("夜来风雨声，\n")
#     f.write("花落知多少。\n")
# finally:
# 3.关闭文件
#     f.close()

#方法二:使用with (推荐方式)
#with语句(上下文管理器)的核心作用就是确保资源的总是被正确获取和释放(即使发生异常,也会被正确释放)
with open("./resources/春晓.txt","w",encoding="utf-8") as f:    #返回值赋给f
    f.write("春晓  [唐] 孟浩然\n")
    f.write("春眠不觉晓，\n")
    f.write("处处闻啼鸟。\n")
    f.write("夜来风雨声，\n")
    f.write("花落知多少。\n")