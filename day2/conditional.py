
# print("This is the conditional statement in python");

# # Conditional statement in python
# # if condition
# a = 22;
# b = 200;
# if b > a:
#     print("b is greater than a");
    
    
# # if-elif condition

# a = 10;
# b = 10;
# if a < b:
#     print("b is greater than a");
# elif a ==  b:
#     print("a and b are equal");
    
    
# # if-elif-else condition
# a = 200
# b = 33
# if b > a:
#   print("b is greater than a");
# elif a == b:
#   print("a and b are equal");
# else:
#   print("a is greater than b");
  
# # example of elif condition
# age = 2;

# if age >= 18:
#     print("You can apply for license");
# elif age < 18:
#     print("You can not apply for the license");
    
# # another example
# light = "blue";

# if(light == "red"):
#     print('Stop');
# elif(light == "green"):
#     print("Go");
# elif(light == "Yellow"):
#     print("Look");
# else:
#     print("Light is not working");

# print("End of code");


# #shorthend if

# if 4 > 2: print("4 is greater than 2");

# a = 2
# b = 330
# print("A") if a > b else print("B");


# marks = int(input("Enter your marks:"));

# if(marks >= 80):
#     grade = "A";
# elif(marks >= 70 and marks < 80):
#     grade = "B";
# elif(marks >= 60 and marks < 70):
#     grade = "C";
# elif(marks >= 50 and marks < 60):
#     grade = "D";
# elif(marks >= 40 and marks < 50 ):
#     grade = "Pass"
# else:
#     grade = "F"
# print("Your grade is", grade);


# # nested if condition

# age = int(input("Enter your age :"));

# if(age >= 18):
#     if(age >= 70):
#         print("You can not drive");
#     else:
#         print("You can drive");
# else:
#         print("You can not drive");
        
        
# # practice questions

# # to check odd or even
# user_input = int(input("Enter the number :"));

# if user_input % 2 == 0:
#     print("Even");
# else:
#     print("odd");
    
    
# to check greatest among 3 numbers;
user_input1 = int(input("Enter the first number :"));
user_input2 = int(input("Enter the second number :"));
user_input3 = int(input("Enter the third number :"));

if(user_input1 > user_input2 and user_input1 > user_input3):
    greatest = user_input1;
elif(user_input2 > user_input3):
    greatest = user_input2;
else:
    greatest = user_input3;
    
print("Greatest number is :", greatest);

# using max() function 

greatest = max(user_input1, user_input2, user_input3);
print("Greatest number is :", greatest);


# to check the multiple of 7 or not 
number = int(input("Enter the number :"));

if(number % 7 == 0):
    print("Multiple of seven");
else:
    print("Not");