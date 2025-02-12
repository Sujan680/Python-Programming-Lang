# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and 
# do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(thisdict)

# len()
print(len(thisdict))

# accessing the items in dict
print(thisdict["brand"])
print(thisdict["model"])
print(thisdict["year"])
print(thisdict["colors"])



my_dict = {
  "name" : "Sujan",
  "age" : 25,
  "marks" : 90,
  "isLoggedIn" : True,
  "subjects" : ("English", "Python", "CSS")
}
print(my_dict["name"])

my_dict["address"] = "Pokhara";
print(my_dict)



## Nested Dict

info = {
  "address" : "Kathmandu",
  "name" : {
    "first_name" : "Sujan",
    "last_name" : "Magar",
  },
  "country" : {
    "city" : "Pokhara",
    "street" : "Chauthe",
    "number" : 14
  }
}

print(info);
print(info["name"]["first_name"])
print(info["country"]["city"])

## update()
info.update({"street" : "Nagdhunga"})

print(info)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.keys()) # retrn the keys
print(car.values()) # return the values of the dict

print(car.items())
print(list(car.items()))
print(tuple(car.items()))

print(car.pop("brand"))

car.popitem() # removes the last item
print(car)