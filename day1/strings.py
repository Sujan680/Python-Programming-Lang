# Strings in python are surrounded by either single quotation marks, or 
# double quotation marks.
# 'hello' is the same as "hello".

print("This is the string in python");

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua.""";
# print(a);

# print(len("hello"));

# # Looping through a string
# a = "HELLO";
# print(len(a));
# for x in a:
#     print(x);
    
    
# # check string

# text = "The best thing in life are free";
# print("free" in text); # True

# # check if not
# text = "The best thing in life are free";
# print("free" not in text); # False
# print("sujan" not in text); # True


# # input in python

# my_name = str(input("Enter your name:"));
# print(type(my_name));
# print("Welcome", my_name);

# my_num = int(input("Enter your fav number:"));
# print(type(my_num));
# print("Your fav number is", my_num);


# a = int(input("Enter your firs number:"));
# b = int(input("Enter your second number:"));

# if a >= b:
#     print(True);
# else:
#     print(False);
    
    
    
# SLicing in Python
# [1:4] here 1 position is included but 4th position is not included

b = "Hello, World";
print(b[1:5]);  # ello
print(b[:4]); # Hell
print(b[2:]); # llo, World
print(b[-1])  # d
print(b[-5 : -2]);  # Wor
print(b[-9:-4]); # lo, W


# String Methods

my_str = "Hello";
print(len(my_str)); # 5

a = "Hello World!";
print(a.upper());
print(a.lower());

# removing white spaces strip()
b = "   Hello, World! "
print(b.strip());

# replace() method
str1 = "This is the best place to visit during summer";
print(str1.replace("summer", "Winter"));

print(str1.index("is"));  # 2

txt = "HELLO, World";
print(txt.split(","));
print(txt.count("L")); # 2
print(txt.capitalize());
print(txt.format());


first_name = "Sujan";
last_name = "Magar";

print(first_name + " " + last_name);


# Format string 

age = 34;
name = "Sujan";
print(f"My name is {name}, I am {age} years old");


# Escape character 

str2 = "This is a string. \"Sujan\" from pokhara"
print(str2);
print(str2[0]);

str = "I am a coder";
print(str.endswith("er")); #True
print(str.endswith("I")); # False
print(str.find("I")); # 0
print(str.find("am")); # 2


str = "Hi I am $ from the $Symbol in the India";
print(str.count("$"));
