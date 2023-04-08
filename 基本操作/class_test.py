class Student:
    name = None
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # def __str__(self):
    #     return f"Student类对象,name:{self.name},age:{self.age}"
stu = Student("star",18)
print(stu)
print(str(stu))