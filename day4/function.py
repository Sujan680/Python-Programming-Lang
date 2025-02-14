
# Functions in python:
# Block of code that perform a specific task;

# syntax:::
# def func_name(param1, param2, ......):
#     some work
#     return val

def my_function():
    print("Hello Python developers")
my_function()

def sum(a,b):
    s = a + b
    return s

print("Sum is:", sum(1,2))


def function(fname, lname):
    print("My name is ", fname + " " + lname)
    
function("Suman","Sharma")



# default parameter
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()


def calc_avg(a,b,c):
    s = int((a + b + c )/3)
    return s
print("The average is :", calc_avg(2,4,6))


# finding the length of a list
nums = [2,4,6,8,10,12,14,16,18,20]

def calc_len(list):
    print(len(list))

calc_len(nums)



def print_list(list):
    for x in list:
        print(x)
      
        nums = [1,2,3,4,5]  
print_list(nums)