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

    def show_all(self):
        if self.stu_list:
            for stu in self.stu_list:
                # Student类的__str__方法已经定义，这里直接调用即可输出学生信息
                print(stu)
        else:
            print('当前没有学生信息')

    def set_score(self):
        sid=input('请输入要设置成绩的学生学号：')
        target=None
        for stu in self.stu_list:
            if stu.stu_id==sid:
                target=stu
                break
        if target:
            socre_str=input('请输入成绩（学科-分数，学科-分数）：')
            score_list=socre_str.replace('，',',').split(',')
            for item in score_list:
                course,score=item.split('-')
                course=course.strip()
                score=score.strip()
                target.add_score(course,float(score))
                print(f'设置成功，{target.name}的{course}的成绩为{score}')
            print(f'设置成功，{target.name}的平均分为{target.calcu_avg()}')
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

    def run(self):
        while True:
            print(self.display())
            choice=input('请输入操作序号：')
            if choice=='1':
                self.add_student()
            elif choice=='2':
                self.delete_student()
            elif choice=='3':
                self.show_all()
            elif choice=='4':
                self.set_score()
            elif choice=='5':
                print('谢谢使用')
                break
            else:
                print('输入错误，请重新输入')


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



m=manager()
m.run()
