# 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# 5. 列出所有学生：遍历所有学生信息并输出。
# 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# 7. 退出系统。

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
