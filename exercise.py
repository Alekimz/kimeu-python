
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
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "email": "john@example.com"
}
print(person)
person.pop("age","city")
print(person)

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









