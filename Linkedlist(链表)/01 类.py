#encoding:utf-8
#Time:2020/10/4 17:41
#Email:1215399218@qq.com
#Author:Mr.jia
#File:01 类.PY
#Software:PyCharm
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print(self.name+'会跑')
a=Dog('花花',2)
a.run()

class Student:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age
    def study(self):
        print(self.name+'在学习')
    def sleep(self):
        print((self.name+'在休息'))
b=Student('小明','男',15)
b.study()
