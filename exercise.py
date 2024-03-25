
"""
my_list=["apple","banana","cherries","grapes","grapes","grapes","mango","apple","banana","watermelon","kiwi","watermelon","strawberry","watermelon","pears","watermelon",]
for i in my_list:
    print(repeat(mylist))
    """

#FINDING LARGEST NUMBERS
list1 = [10, 20, 4, 45, 99]
print("Largest element is:", max(list1))

#TUPPLE
mylist=('subaru','bmw','v.wagon','mercedes','audi')
print(mylist)
mycarlist=list(mylist)
print(mycarlist)
mycarlist.append('faw')
print(mycarlist)
mylist=tuple(mycarlist)
print(mylist)


#DICTIONARIES
#deleting a number of keys  #MODE
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@example.com"
}
print(person)
delete_keys=("age","city")

for key in delete_keys:
    del person[key]
print("my new person details are:",person)


#KOECH
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@example.com"
}
print(person)
del person["age" and "city"]
print("koech person is:",person)

#cheking existence
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@gmail.com"
}
if "John" in person.values():
    print("Yes, 'john' is one of the values in the person dictionary")

#conversion
mylist1=["apple","banana","cherry"]
mylist2=["6","8","10"]
res = {mylist1[i]: mylist2[i] for i in range(len(mylist1))}
print("Resultant dictionary is : " + str(res))



#SETS
#add items
Mycarz= {"benz", "v.wagon", "audi"}
print(Mycarz)
Mycarz.add("Eicher")
print(Mycarz)

#REMOVE ITEMS
Mycarz= {"benz", "v.wagon", "audi","mazda","vitz"}
print(Mycarz)
Mycarz.remove("audi")
print(Mycarz)

#GETTING RREPEATED ELEMENT
my_list = ["apple", "banana", "cherry", "banana", "apple", "banana"]
repeated_my_list = set()
None_repeated_my_list=set()
for itm in my_list:
    if my_list.count(itm) > 1:
        repeated_my_list.add(itm)
    else:
        None_repeated_my_list.add(itm)
print("the repeated items are:",repeated_my_list)
print("the none repeated items are:",None_repeated_my_list)



#AOB
   #if error occurs else is not executed and vice versa
      #Exception as e shows which error youve committed
number1=0
number2=20
try:
    x=number2/number1
except Exception as e:
    print("ushaakosea mahn:",e)
else:
    print(x)
    print("all is well")



number1=0
number2=20
try:
    x=number1/number2
except Exception as e:
    print("ushaakosea mahn:",e)
else:
    print(x)
    print("all is well")








