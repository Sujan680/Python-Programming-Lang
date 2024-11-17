# Data Types in PYthon

x = "Hello world"
print(type(x))  #string

num = 20
print(type(num))  #Integer

num2 = 34.3
print(num2)
print(type(num2)) #Float

x = 1j
print(x)
print(type(x)) #Complex

x = ['apple', 'banana', 'mango']
print(x)
print(x[1])
print(type(x))  # List Type

x = ( "apple" , "ball" , "banana")
print(type(x)) # Tuple type


x = range(5)
print(x)
print(type(x)) # Range type

x = True
print(type(x))  #Boolean type

x = None
print(type(x)) # Nontype


#Setting Specific Data types 

x = str('Helllo World')
print(x)

x = int(20.34)
print(x)

x = bool(4)
print(x)

x = 34
a = float(x)
print(a)