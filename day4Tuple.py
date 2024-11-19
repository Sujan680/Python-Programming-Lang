# A tuple in python is a collection of items which is ordered, immutable
#  and allows duplicate elements

# Creating a tuple in Python

empty_list = ()
print(empty_list)

single_list = (1,)
print(single_list)

multiple_list = (1,2,"apple", True)
print(multiple_list)

#Accessing tuple items

my_tuple = (1,2,3,4,5,6)

print(my_tuple[-1])
print(my_tuple[2:])
print(my_tuple[:4])


tuple1 = (1,2,3)
tuple2 = ('app', 'bus')
print(tuple1 + tuple2)

print(2 in tuple2)  # false


# Unpack in tuples

my_tuple = (1,2, "Hello", "sujan", True, False,1 ,2)

(a,b,*c) = my_tuple

print(a)
print(b)
print(c)


# Methods in Python 

print(my_tuple.count("Hello"))
print(my_tuple.index(1))