class Student:
    def __init__(self):
        print("constructor called")

    def self_student_name(self,name):
        self.student_name=name

    def display_student_name(self):
        print("student name:",self.student_name,)

    def self_student_age(self,age):
        self.student_age=age

    def display_student_age(self):
        print("student age:",self.student_age)

student1=Student()
student1.self_student_name("Alex")
student1.display_student_name()
student1.self_student_age("23")
student1.display_student_age()


class Student:
    def __init__(self,name,age):
        self.student_name = name
        self.student_age = age
    print("constuctor called")

    def display_student_details(self):
        print("student:",self.student_name,"age:",self.student_age)

student1=Student(name="Alex",age="23")
student1.display_student_details()




