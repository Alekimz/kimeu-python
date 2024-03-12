#variables
student_name ="alex" #data type is string
student_age ="23" #data type is integer
student_marks ="65" #data type is integer
is_male= True #data type is boolean
student_fee =100.0 #data type is float

#outputting the values in the variables
print(student_name)
print(student_age)
print(is_male)

student_name ="alex"
student_name ="ann"
print(student_name)

#case sensitivity
STUDENT_NAME ="Mercy"
student_name ="Kelvin"
print(STUDENT_NAME)


#variable naming in python
book_price=20.0 #valid variable name
_book_price=20.0 #valid variable name


x=y=z=10 #assigning one value to multiple variables
x,y,z=30,40,50 #multiple values being assigned to multiple variables

x=10
X=14
print(x)
print(X)

x=10
x=267
print(x)



price=10
qty=7
total=price*qty
myanswer1="the total is:"+str(total)+" kenya shillimgs"
print(myanswer1)


firstname="alex"
secondname=787878
thirdname=firstname+" "+str(secondname)
print("my third name is "+thirdname)


firstname="alex"
secondname=("kimeu")
thirdname=firstname+" "+secondname
print("my third name is "+thirdname)


#assignment operators
x=5
print(x)
x+=5 #x=x+5
print(x)
x-=4 #x=x-4
print(x)
x*=3 #x=x*3
print(x)
x/=2 #x=x/2
print(x)

#COMPARISON OPERATORS
a=20
b=15
print(a==b)

#LOGICAL OPERATORS
age=20
nationality="North america"

if nationality=="kenya" and age>35:
    print("you can be president")
else:
    print(" you cannot be president")


age = 37
nationality = "kenya"

if nationality == "kenya" and age > 35:
    print("you can be president")
else:
    print(" you cannot be president")

age=26
region ="embakasi,westlands,kasarani"

if region=="Embakasi"or"Westlands"or"Kasarani":
      print("you can be governor")

else:
     print("you cannot be governor")





