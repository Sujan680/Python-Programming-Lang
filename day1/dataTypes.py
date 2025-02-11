
# In programming, data type is an important concept.
# Variables can store data of different types, and different types 
# can do different things.
# Python has the following data types built-in by default, 
# in these categories:

print("THis is the data types in Python")
# Text Type:	str

hello_world = "Hello World";
print(hello_world);
print(type(hello_world));

# Numeric Types:	int, float, complex
myNum = 234;
print(myNum);
print(type(myNum)); #int

my_Num = 33.33;
print(my_Num);
print(type(my_Num)); #float

complex_number = 1j;
print(complex_number);
print(type(complex_number));

# Sequence Types:	list, tuple, range

my_list = ['apple', 'banana', 'cherry'];
print(my_list);
print(type(my_list)); # list type <class 'list'>
print(my_list[0]); #accessing item at 0 index
print(my_list[1]);
print(my_list[2]);


my_tuple = ('ram', 'hari', 'santosh', 'dipesh');
print(my_tuple);
print(type(my_tuple));
print(my_tuple[1]);

my_range = range(6);
print(my_range); # range(0,6)
print(type(my_range)); # range type

# Mapping Type:	dict

my_info = {"name": "Sujan", "age": 26, "address": "Pokhara"};
print(my_info);
print(type(my_info));
print(my_info['name']); #accessing the dict's items

# Set Types:	set, frozenset

my_set = {"apple", "mango", "watermelon", "juice"};
print(my_set);
print(type(my_set));

my_frozenset = ({"hi", "ram", "fine", "banana"});
print(my_frozenset);
print(type(my_frozenset));

# Boolean Type:	bool
isLoggedIn = True;
print(isLoggedIn);
print(type(isLoggedIn));

# Binary Types:	bytes, bytearray, memoryview
x = b"Hello";
print(x);
print(type(x));

x = bytearray(5);
print(x);
print(type(x));

x = memoryview(bytes(5));
print(x);
print(type(x));

# None Type:	NoneType
x = None;
print(x);
print(type(x));


#Setting th specific data types

#setting the string data types
my_str = str("Hello World");
print(my_str);
print(type(my_str));

# setting the int data types
my_num = int(12.45);
print(my_num);

num1 = float(123);
print(num1);

x = complex(3j);
print(x);

# setting the list type

list_type = list(["apple", "banana", "cherry"]);
print(list_type);

tuple_type = tuple(("apple", "banana", "cherry"));
print(tuple_type);
print(tuple_type[2]);

# setting type dict
x = dict({"name": 'sujan'," age": 12});
print(x);
print(type(x));

# setting the set type

set_type = set({"sujan", "dipesh", "ram", "high"});
print(set_type);
print(type(set_type));

isBol = bool(0); # false
print(isBol);


x = 35e3
y = 12E4
z = -87.7e100

print(type(x));
print(type(y));
print(type(z));

# to input name
# first_name = str(input("Enter your first name"));
# print(first_name);


