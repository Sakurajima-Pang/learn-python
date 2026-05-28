from abc import ABC,abstractmethod

class say:
    @abstractmethod
    def speak(self,msg):
        pass

# print(f'{type(say)}')

class Person(say):
    def __init__(self,name) -> None:
        self.name=name

    # def __str__(self) -> str:
    #     return f'他是{self.name}，他是一个人类对象'
    
    def speak(self,msg):
        print(f'{self.name}在说：{msg}')

# print(f'{type(Person)}')


class animals:
    def __init__(self,name) -> None:
        self.name=name

    # def __str__(self) -> str:
    #     return f'它是{self.name}，它是一个动物对象'
    
    def speak(self,msg):
        print(f'{self.name}在叫：{msg}')

# print(f'{animals}')

def make_sound(obj,msg):
    obj.speak(msg)

p1=Person('pang')
a1=animals('dog')

# print(p1)
# print(a1)
# print(p1.__dict__)
for attr in dir(p1):
    print(attr)

# print(f'{type(p1)}')
# print(f'{type(a1)}')

make_sound(p1,'你好')
make_sound(a1,'汪汪')


list1=[1,2,3]
print(f'{type(list1)}')