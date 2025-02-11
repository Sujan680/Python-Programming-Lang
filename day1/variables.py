# This is the comment , # hash is used, To make code readable

# Variables are containers for storing data values. 
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables name are case sensitive

x = 45;
y= "John";
print(x);
print(y);


# Casting : to specify the type of a variable
# to check type we use type() function
x = str(3);
print(x);
print(type(x));

y = int(3);
print(y);
print(type(y));

z = float(3);
print(z);
print(type(z));

myName = "Sujan";
print(myName);

my_variable_name = "John";
print(my_variable_name);


# Assigning multiple variables in one line 

x,y,z = "Orange", "Banana", "Cherry";
print(x);
print(y);
print(z);

# assign the same value to multiple variables in one line

x = y = z = "Hi, I am sujan magar";
print(x);
print(y);
print(z);

# Unpack a collection:
# Python allows you to extract the values into variables. 
# This is called unpacking.
fruits = ["Orange", "Apple", "Banana"];
x,y,z = fruits;
print(x);
print(y);
print(z);


# using + operator

x = "Python "
y = "is "
z = "awesome"
print(x + y + z); # Python is awesome

x = 5
y = 10
print(x + y); # 15 

# x = 5
# y = "John"
# print(x + y); # it will throw error

x = 5
y = "John"
print(x, y)  # 5 John


# Global variable

x = "Sujan";

def myfunc():
    print("My name is", x); # print("My name is" + x)
    
myfunc();

# Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x);

my_name = "The name of Python developer is Guido Van Russom";

print(f"{my_name} which is developed in 1991");

print("""Hi, this is the multi line
      printing in python""");


print("Hi, this is Sujan \n I am from Pokhara");


a = "Hello World!!";
print(a);