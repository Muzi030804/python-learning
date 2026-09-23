# csv操作 - 方式一:
# 写
with open("csv_data/01.csv", "w", encoding="utf-8") as f:
    f.write("姓名,年龄,性别,爱好\n")
    f.write("小王,18,男,'football,java'\n")
    f.write("小李,20,女,Python\n")

# 读
with open('csv_data/01.csv', 'r', encoding="utf-8") as f:
    for row in f:
        print(row.strip())

#csv操作 - 方式二:(推荐)
import csv

#写
with open("csv_data/02.csv", "w", newline="") as f:
    writer = csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader()    #写入表头
    writer.writerow({"姓名":"小王","年龄":18,"性别":"男","爱好":"football,Java"})  #写入数据
    writer.writerow({"姓名":"小李","年龄":20,"性别":"女","爱好":"Python"})  #写入数据

#读
with open("csv_data/02.csv","r",encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)