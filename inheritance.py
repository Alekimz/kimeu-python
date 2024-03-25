#PARENT CLASS
class person:
    age=""
    name=""
    uniform=""
    def __init__(self,age,name,uniform): #CONSTRUCTOR
        self.age = age
        self.name= name
        self.uniform= uniform

    def printperson(self):
        print("the details of the vehicle are:",self.age,self.name,self.uniform)

#CHILD CLASS
class student(person):
    pass
    def __init__(self,age,name,uniform): #STUDENT CONSTRUCTOR
          super().__init__(age,name)  #MAKING REFERENCE TO PARENT CLASS
          self.uniform=uniform

#student1=student(name="alex",age=20,uniform="khaki")
student.printperson(person)


