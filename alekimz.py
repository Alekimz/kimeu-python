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





def is_odd(number):
    return number % 2 != 0

x= 7

if is_odd(x):
    print(f"{x} is odd.")
else:
    print(f"{x} is even.")


y=200
x=2
ans=y%x
print(ans)
if ans==0:
    print("y is an even number")
else:
    print("y is an odd number")


y=209
x=2
ans=y%x
print(ans)
if ans==0:
    print("y is an even number")
else:
    print("y is an odd number")

""""
y= int(input("enter your number to be checked:"))
x=2
ans=y%x
print(ans)
if ans==0:
    print("y is an even number")
else:
    print("y is an odd number")
"""

"""
country=input("enter your country:")
if country=="Rwanda":
    print("East African")
elif country=="Kenya":
    print("East African")
elif country=="Congo":
    print("East African")
else:
    print("invalid country")
"""







#LOOPS
#the while loop
x=1
while x<=5:
    print("Alex")
    x+=1


x=1
while x<=5:
    if x==3:
        break
    print("x")
    x+=1


#continue statement in while loop
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
        print(i)

"""
x=1
while x<=10:
    print("the number is:",x)
    x+=1
else:
    print("loop ended")
"""

x=1
while x<=10:
    if (x==3):
            break
    print("the number is:",x)
    x+=1
print("loop ended")


"""
x=1
while x<=10:
    if (x==3):
            break
    print("the number is:",x)
    x+=1
    print("loop ended")
"""


x=1
while x<=10:
    if x == 3 or x == 5:
        x+=1
        continue
    print("the number is:",x)
    x+=1
print("loop ended")


numbers=[1,3,5,7,9]
total=0
for num in numbers:
    total += num
print("the sum of numbers  odd numbers is",total)

"""
x=1
while x<10:
     if x%2=="1":
      total += num
print("the sum of numbers is",total)
"""


"""
i=0
sum=0
while i<=10:
    if i%2==1:
     sum=sum+i
    i=i+1
print("the total sum is",sum)
"""
"""
total=0
for num in range(10):
    if num%2!=0:
     total=total+num
print("the total sum of all odd numbers  is",total)

"""

"""
names=[]
num_names = int(input("How many names do you want to enter? "))
for i in range(num_names):
        name = input("Enter your name: ")
        names.append(name)
for name in names:
    print(name)
"""


"""
input[input("Enter your name:"),input("Enter your name:"),input("Enter your name:")]
print(input)
"""

#DICTIONARIES
#Acessing a value from a dictionary,we specify the key of that value
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)