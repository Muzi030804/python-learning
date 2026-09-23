from lxml import html
import csv
# with open("resources/仙逆人物志.html","r",encoding="utf-8") as f:
#     html_text = f.read()
# doc = html.fromstring(html_text)
#
# rw_list = doc.xpath("//table/tbody/tr")
#
# for rw in rw_list:
#     # 相对当前行提取姓名
#     name_list = rw.xpath("./td[1]/text()")
#     name = name_list[0].strip() if name_list else "未知姓名"
#     # 相对当前行提取头像地址
#     img_list = rw.xpath("./td[3]/img/@src")
#     img_url = img_list[0] if img_list else "无头像"
#     print(f"{name} | {img_url}")
#
# print(f"人物总数：{len(rw_list)}")

# 读取并解析HTML
with open("resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_text = f.read()

document = html.fromstring(html_text)

# 获取所有人物行
person_rows = document.xpath(
    "//div[@class='table-container']/table/tbody/tr"
)

fieldnames = ["姓名", "性别", "修为", "头像"]
characters = []

# 每个人物行转换成一条字典记录
for row in person_rows:
    name_list = row.xpath("./td[1]/text()")
    gender_list = row.xpath("./td[2]/text()")
    avatar_list = row.xpath("./td[3]/img/@src")
    level_list = row.xpath("./td[4]/text()")

    character = {
        "姓名": name_list[0].strip() if name_list else "",
        "性别": gender_list[0].strip() if gender_list else "",
        "修为": level_list[0].strip() if level_list else "",
        "头像": avatar_list[0].strip() if avatar_list else "",
    }

    characters.append(character)

# 写入CSV
with open(
    "csv_data/characters.csv",
    "w",
    encoding="utf-8",
    newline=""
) as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(characters)

# 重新读取CSV并验证
character_count = 0

with open(
    "csv_data/characters.csv",
    "r",
    encoding="utf-8"
) as f:
    reader = csv.DictReader(f)

    for character in reader:
        print(character["姓名"])
        character_count += 1

print(f"人物总数：{character_count}")