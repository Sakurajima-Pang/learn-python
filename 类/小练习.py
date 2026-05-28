from datetime import datetime


class manager:
    
    def __init__(self) -> None:
        self.stu_list=[]

    def add_student(self):
        name=input('请输出姓名：')
        age=input('请输出年龄：')
        gender=input('请输出性别：')
        stu=Student(name,age,gender)
        self.stu_list.append(stu)
        print(f'添加成功，{stu.name}的学号为{stu.stu_id}')

    def delete_student(self):
        sid=input('请输入要删除的学生学号：')
        target=None
        for stu in self.stu_list:
            if stu.stu_id==sid:
                target=stu
        if target:
            self.stu_list.remove(target)
        else:
            print(f'没有找到学号为{sid}的学生')

    def display(self) -> str:
        menu = []
        menu.append(f"--- 学生管理系统 ---")
        menu.append("1. 添加学生")
        menu.append("2. 删除学生")
        menu.append("3. 查看所有学生")
        menu.append(f"4.输入课程和成绩")
        menu.append("5. 退出")
        menu.append("请输入操作序号")
    
        return "\n".join(menu)



class Person:
    def __init__(self,name,age,gender) -> None:
        self.name=name
        self.age=age
        self.gender=gender

class Student(Person):
    
    count=0

    def __init__(self,name,age,gender) -> None:
        super().__init__(name,age,gender)
        Student.count += 1
        self.stu_id=f'{datetime.now().year}{Student.count:03d}'
        self.scores={}

    def __str__(self) -> str:
        return f'''学生姓名：{self.name}，年龄：{self.age}，性别：{self.gender}
学号：{self.stu_id}，{self.calcu_avg()}'''

    #add方法
    def add_score(self,course,score):
        self.scores[course]=score


    # 计算平均分
    def calcu_avg(self):
        if self.scores:
            return f'{sum(self.scores.values())/len(self.scores):.2f}'
        else:
            return f'没有成绩记录'




s1=Student('张三',18,'男')
s1.add_score('语文',85)
s1.add_score('数学',90)
s1.add_score('英语',88)
print(s1.calcu_avg())
s2=Student('李四',19,'女')
print(s2.calcu_avg())



