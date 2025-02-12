# Set is a collection which is unordered, unchangeable*, and unindexed.
# No duplicate members.(unique values stores)

nums = {1,2,3,4,5}
print(nums)
print(len(nums))
print(type(nums))

## any types of data types but not list, dict
collections = {1,22,33, 22, "Sujan", "Magar", True}
print(len(collections))


######## creating empty set #######

empty_set = set();
print(type(empty_set))
print(len(empty_set)) # 0

###### Set Methods --- add(), remove(), clear(), pop()

empty_set.add("Apple")
empty_set.add("Car")
# empty_set.add("Apple", "Ball")  #set.add() takes exactly one argument (2 given
print(empty_set) # {"Apple", "Car"}


empty_set.remove("Car");
print(empty_set)


arrr = {1,2,3,4,5}
arrr.clear() # empties the set
print(arrr)

arrr = {4,5,4,53, "Sujan"}
arrr.pop()
print(arrr)


# QSn

my_dict = {
    "table" : ["a piece of a furniture", "list of facts and Figures"],
    "cat" : "a small animal"
}
print(my_dict);


# enter 3 marks and then store in the dict
marks = {};
mark1 = input("Enter your marks");
marks.update({"phy" : mark1})
mark2 = input("Enter your marks");
marks.update({"scie" : mark2})
mark3 = input("Enter your marks");
marks.update({"social" : mark3})

print(marks)


