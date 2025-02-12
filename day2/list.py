
# Lists are used to store multiple items in a single variable.
# List items are ordered, changeable, and allow duplicate values.
# It can store elements of different data types (int, float, string, complex, bol etc..)

my_list = ["apple", "ball", "mango"];
print(my_list);
print(type(my_list));
print(len(my_list));

marks = [12,45,66,44,55,90]
print(marks);
print(marks[0]);
print(marks[1]);
print(marks[2]);
print(marks[3]);

students = [56, "Sujan", "Hi", 1j, True, False, 44.5]
print(students);
students[1] = "Namita";
print(students);


# list slicing 
print(students[1: 3]);
print(students[3:])
print(students[-3:-1]);

# list methods --- append, sort, reverse, insert()...
my_numbers = [2,5,0, 1, 45, 67];
my_numbers.append(23)
print(my_numbers)

my_numbers.sort();
print(my_numbers)

my_numbers.sort();
my_numbers.reverse();
print(my_numbers);

# insert into specific index
my_numbers.insert(-1,100);
print(my_numbers);

# pop methods

my_numbers.pop(); # removes the last items
print(my_numbers)

my_numbers.pop(2); # removes the 2 indexed item
print(my_numbers)


# The list() Constructor;

# note the double round-brackets
list = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")) 
print(list)
print(list[1]) #banana
print(list[-1]) # cherry
print(list[-6: -1]);

# checking if item exists

print("apple" in list);


# change the values using range

list[2:4] = ["blackcurrant", "watermelon"];
print(list)

# extend
list_1 = [1,2,3];
list_2 = [4,5,6];
list_1.extend(list_2);
print(list_1) #  [1,2,3,4,5,6]

# remove : remove the specific item
list_1.remove(4);
print(list_1)



#  Loop through a list

list = [1,2,3,4,5,6,7,8,9,10];
for x in list:
    print(x);
    
# through indexed nmber

for i in range(len(list)):
    print(list[i])

# Copy a list
thislist = ["apple", "banana", "cherry"]

mylist = thislist.copy()

print(mylist)

