
# String in python 

# str1 = 'This is string in Python'
# print(str1)

# str2 = "Sujan Magar"
# print(str2)

# str3  = '''Hi i am sujan
# from the top of the world
# and land of Mountains'''
# print(str3)

# a = "Hellow World"
# print(len(a))

# for i in a:   #loop through the strings "Hello World"
#     print(i)

txt = "the best thing in life are free!"
print(txt.capitalize())

print(txt.upper())
print(txt.lower())

if "free" in txt:
    print("Yes it is present")
else:
    print("Is not present")

#Slicing: start and end index should be specified 

b = "Hello World"
print(b[1:4]) #ell
print(b[2:])  #llo World
print(b[:5])  #Hello


a = "  Hello Sujan"
print(a)
print(a.strip())  #to remove whitespaces
 
print(a.replace("Hello", "Hi").strip())


print(a.split(" "))  # split the string into substring


## Concatenation String

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# F-string in Python: formating string
age = 33
txt = f"My name is Sujan and I am {age}"
print(txt)
price = 60
txt = f"The price is ${price} dollars"
print(txt)


myTxt = "Hey this is sujan"
print(myTxt.count("Hey"))  # Returns the numbr of times "Hey" appears in the string

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 1, 24)

print(x)


# To find the odd or even numbers 
# myInput = int(input("Enter first number:"))
# rem = myInput % 2

# if(rem == 0):
#     print("Even")
# else:
#     print("Odd")

# # To find the greater among the 4 numbers
# first = int(input("enter first num:"))
# second = int(input("enter second num:"))
# third = int(input("enter third num:"))
# fourth = int(input("enter fourth num:"))

# if(first >= second and first >= third and first >= fourth):
#     greater = first
# elif(second >= third and second >= fourth):
#     greater = second
# elif(third >= fourth):
#     greater = third
# else:
#     greater = fourth

# print("Greater num is :", greater)