import random
from itertools import count
from operator import indexOf

# print("Hello World In Pyhon Programming Language")  # Single Line comment

"""
But In Python I can use tripple line string for explaining stuff describtively

"""

# And This is another single line comment
# I can Add So many comment as i want


"""
Python Varibale is container for storing data/value whatever you say
- In Variable You Can Store Any Type Of Data That Support In A Programming Language
----- Some Example------

* String
* Number/ Integer whatever you say
* Floating Number / Decimal Number
* Boolean Like True Or False
-- Here Is More Details
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType

"""


# Creating Variable Will Be Like

variableName = "This is variable name"  # This variable contain string


variableForInteger = 63  # This one is contain integer value

"""
So How Can I Check the variable type ??????? Big Concern Right..

There is an awesome way in python that called type casting


"""
# checkSting = "This is strign type"
# print(type(checkSting))


# Suppose I Want To Convert Any  integer  to  String

# LETS TRY
"""

intVal = 63
intToString = str(intVal)

print(type(intToString))  # It will return string

"""

"""
3 ways I can do type casting in python programming language

-- int() for converting floating, decimal  number to direct integer

-- float() for converting any integer number to floating point number
--  str() for converting anything to string

"""


# Unpack List Into variable like this one

# fruits = ["apple", "banana", "mango"]

# x, y, z = fruits

# print("Printing  Fruits Name " + " " + y)


"""
 Global Variable

 -- Is type of variable which can be accesed from every where from the program file, From inside the function to outside the function

 -- global keyword use for defining global variable in a specific function
"""

# Globale Variable

"""

def checkGlobal():
    global GlobalOne   # Globale variable by global keyword
    GlobalOne = "one "
    print("Printing inside funciton ", GlobalOne)


checkGlobal()

print("Printing outside funciton ", GlobalOne)


print("=========================================================")


x = 1sf

print(type(x))

"""


# print(random.__all__)
# print("---------------------------------------")
# print(random.choice)


# wow wow wow , I can assign multiline string in variable

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

# print(a)


# Accecing string in various way

stringx = "hello world"
# print(len(stringx))
# print(stringx[0:len(stringx)])


# for x in stringx:
#     print(x)


# # conditional string

# freeString = "Programming will  makes you independent "


# if "will" in freeString:
#     print("Yes  will  present there")


"""
Modifying string

---


"""


# myTuple = ("John", "Peter", "Vicky")

# x = " - ".join(myTuple)
# print(x)


# # Escaping

# escapedString = "My NAME IS \"Md Sowrov \" "
# print(escapedString)


# List in python


thislist = list(["apple", "banana", "cherry", "moglai", "cherry"])

"""
[] List are used to store multiple value in a single variable

[] List items is ordered , changable and allow to duplicate the value

[] List items can be any data type

"""
# print(type(thislist))

print(thislist[0])


# Print the length of list

print(len(thislist))

if "apple" in thislist:
    print("Yes !! Apple Exist")

else:
    print("Nope nothing there ")


# change the list items in specicific index

thislist[2] = "orrange"


print("New List", thislist)


# insert items

thislist.insert(0, "Cherry")

print("After Inserting", thislist)


# add items in list


thislist.append("This is added by append method ")
print("--------")


print(thislist)


# remove items from the list


thislist.remove("apple")
print("After removing apple ", thislist)

# pop will remove the last element by default but it takes index that which element should remove

thislist.pop()
thislist.pop(0)

print("After poping last & fast  element of the list", thislist)


# clear the whole list

thislist.clear()

print(thislist)


# Create New List From this list
print("================= After Creating New List From Scratch===========")

thislist.append("Js")
thislist.append("Python")
thislist.append("React Js")
thislist.append("Node Js")
thislist.append("CSS3")
thislist.append("Problem solving")

print(thislist)

# loop through the list


# for x in thislist:
#     print(x)


# Another way to loop through in a list


# for i in range(len(thislist)):
#     print(thislist[i])


# Using while loop


# i = 0

# while i < len(thislist):
#     print(thislist[i])

#     i += 1


# Using List Comprehension

# [print(x) for x in thislist
#
print("-----")
newlist = []


for x in thislist:
    if "o" in x:
        newlist.append(x)


print(newlist)


# extending list

list1 = ["a", "b", "c"]

list2 = [1, 2, 3]


list1.extend(list2)
print(list1)


"""
Python tuples



"""


thistuple = ("apple", "banana", "cherry", "apple")
x1 = list(thistuple)  # convert into list
x1.append("something ")  # appending value into list

thistuple = tuple(x1)  # then again convert into touple
print(thistuple)  # And Finally Print it


print(thistuple.count("cherry"))
print(thistuple.index("cherry"))


# set


thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

for x in thisset:
    print(x)


# dictionary

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict.get("model"))
x = thisdict.keys()
print(x)
thisdict["nice"] = "Really Nice "


print(thisdict.keys())
