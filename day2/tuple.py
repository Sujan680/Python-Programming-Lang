
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

print("This is a tuple in Python");

tuple = (1,2,3,4,5)
print(tuple)
print(tuple[0])
print(tuple[1])
print(tuple[2])

# tuple[0] = 4; unchangeable
print(tuple)

# allow duplicate value
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))


### Creating tuple with one item

my_tuple = ("Sujan",)
print(my_tuple)

tuple1 = ("abc", 34, True, 40, "male")
print(type(tuple))


###Tuple constructor tuple()

tuple2 = ((1, 'cherry', True, 4.5))
print(tuple2)
print(type(tuple2))

#Tuples are unchangeable, meaning that you cannot change, add, or 
# remove items once the tuple is created.

# x = ("apple", "banana", "cherry")
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)

# print(x)


# thistuple = ("apple", "banana", "cherry")
# y = list(thistuple)
# y.append("orange")
# thistuple = tuple(y)


# Unpacking in tuple 

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


### Using * Asterik
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

print(green.index("apple"))
print(yellow.index("banana"))
print(red.index("raspberry"))

print(red.count("raspberry"))


# slicing in tuple is similar to the list 

fav_movies = [
    input("Enter your 1 st fav movie"),
    input("Enter your 1 st fav movie"),
    input("Enter your 1 st fav movie")
];

my_list = [];

my_list.append(fav_movies)
print(my_list)


## to check palindrome or not
list1 = [1,2,3,1,1];
list2 = list1.copy();

list2.reverse();

if list1 == list2:
    print("Palindrome")
else:
    print("not palindrome");
    
    
    ## to count number of A
tuple_count = ("C", "D","A","A","B","B", "A");

print(tuple_count.count("A"));


my_list = list(tuple_count);

my_list.sort();
print(my_list)