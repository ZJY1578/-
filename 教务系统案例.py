#Day One
#学生


class Students :
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

#对于显示形式

    def __str__(self) -> str:
        return f"姓名:{self.name}|语文:{self.chinese}|数学:{self.math}|英语:{self.english}"

#Day two 对于教务系统

    def update_score(self,chinese =None ,math = None ,english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

class EducationSystem:
    EducationSystem_ver = 1.0

    def __init__(self):
        self.list_student = []

    def add_student_score(self):
        name = input("请输入学生姓名：")
        for s in  self.list_student:
            if s.name == name:
                print("该学生已在数据库中请勿重复添加")
                return

        chinese = float(input("请输入该学生语文成绩："))

        math = float(input("请输入该学生数学成绩："))

        english = float(input("请输入该学生英语成绩："))

        if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
            stu = Students(name, chinese, math, english)
            self.list_student.append(stu)
            print("该生添加成功")
            return
        else:
            print("数值错误 分数应均在0至150内")
            return

#修改学生分数
    def update_student(self):
        name = input("请输入要修改的学生的姓名：")
        for s in self.list_student:
            if s.name == name:
                print(f"该生成绩为{s}")
                chinese = int(input("请输入该学生语文成绩："))

                math = int(input("请输入该学生数学成绩："))

                english = int(input("请输入该学生英语成绩："))
                if 0 <= chinese <= 150 and 0 <= math <= 150 and 0 <= english <= 150:
                    s.update_score(chinese,math,english)
                    print("成绩修改成功")
                    print(f"修改后的成绩为{s}")
                    return
                else:
                    print("成绩超出范围请重新输入")
                    return
        print("该生不在数据库中，请添加")

    #删除学生成绩
    def delete_student(self):
            delete1 = input("请输入要删除成绩的学生")
            for s in self.list_student:
                if s.name == delete1:
                    self.list_student.remove(s)
                    print("删除成功")
                    return
            else:print("未查到该生")

    def seek_student(self):
        name = input("请输入查找的学生名")
        for s in self.list_student:
            if s.name == name:
                print(f"{s}")
                return
        else:print("未查找到该生")

    def seek_all_student(self):
        for s in self.list_student:
            print(f"{s}")

#运行代码
    def run(self):
        while True:
            print("运行中 欢迎使用Edu系统")
            print()
            print("#############################################")
            print("# 1.添加 2.修改 3.删除 4.查询指定 5.查询所有 6.退出#")
            print("#############################################")

            act = input("请输入执行代码")
            try:
                match act:
                    case "1":
                        self.add_student_score()
                    case "2":
                        self.update_student()
                    case "3":
                        self.delete_student()
                    case "4":
                        self.seek_student()
                    case "5":
                        self.seek_all_student()
                    case "6":
                        break
                    case _:
                        print("输入错误")
            except Exception:
                print("错误")


if __name__ == "__main__":
    education_system = EducationSystem()
    education_system.run()


