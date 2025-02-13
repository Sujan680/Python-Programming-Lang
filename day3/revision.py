
################ Strings ###########

str1  = "Hello"
str2 = "World"
print(str1 + " " + str2)

my_str = "Hi I am sujan magar"
print(len(my_str))
print(type(my_str))

print(my_str[0])
print(my_str[1])
print(my_str[5])


# slicing 

str = "Hello"
print(str[1:3])
print(str[:3])
print(str[2:])
print(str[-3:-2])

########## string functions

str = "I am a coder"
print(str.endswith("I"))

print(str.endswith("coder"))

print(str.capitalize())

print(str.lower())

print(str.replace("I", "I'm"))
print(str.find("coder"))

str = "            sujan  "
print(str.strip())

####### List in python ##########
# A built in data types that stores set of values

marks = [12,56,78,90,34]
marks[4] = 99
marks[2] = 59
print(marks)
print(len(marks)) # 5

## Slicing ----- similar to the strings

marks = [1,2,3,4,5,6,7,8,9,10]
print(marks[2: 6])
print(marks[: 6])
print(marks[2: ])
print(marks[:-1 ])
print(marks[-5: ])


### List methods

lists = [11,22,33,100,44,55,66,77, 0, 56, 10];

lists.append(99)
print(lists)

lists.sort()
print(lists)

lists.insert(10, 400)  # insert at index 10 
print(lists)

print(lists.reverse()) ## None :: doesnot support or doesnot return
lists.reverse()
print(lists)

# removing items 

list = [2,5,7,10]
list.remove(2) # removes the 2 value from list
print(list)

list.pop(2)  # remove 2 indexed value that is 10 [5,7,10]
print(list)