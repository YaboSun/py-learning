from types import MethodType


class Student(object):
    pass


s1 = Student()
s1.name = "Michael"
print(s1.name)


def set_age(self, age):
    self.age = age


Student.set_age = set_age
s1.set_age(20)
print(s1.age)

s2 = Student()
s2.set_age(25)
print(s2.age)

