
# List in Python : Lists are used to store multiple items in a single variable
# list are built-in data types in python
# Used to store collections of data that are ordered, mutable and allow duplicate elements

myList = []  # Empty list
print(myList)

numbers = [1,2,3,4,5]  # List with integers
print(numbers)

mix_list = [1, 'Hello', 3.12, True]  # List with mixed data types
print(mix_list)


# Accessing  elements in list: we use indexing to access elements

print(mix_list[2])
print(numbers[-1])  # [-1] indicates the last element in list
print(mix_list[0])  # [0] indicates the first element in the list

# Modifying a List

list = [1,2,3,'Hi', 'sujan', True, False, 10]

list[2] = 'Magar'
print(list)

list.append("100")  # append method insert the items at the end of the list
print(list)

list.insert(5, "Python")  # insert element at index 5 
print(list)

list.pop(0)  # removes specified  indexed item 
list.remove("Hi")
print(list)

# Methods in List

print(type(list))

print("The length of the list is:",len(list))