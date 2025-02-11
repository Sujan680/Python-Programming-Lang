print("This is the operator in python");

# Arithmetic operator
# Relational or Comparison operator
# Assignment Operator
# Logical Operator

print(2 + 3);
print(2 * 3);
print(21 - 3);
print(21 / 3);
print(45 % 3);  #remainder finding
print(2**3);  # power a^b = 2^3
print(15//2); # 7

a = 12;
b= 8;
print(a >= b);
print(a <= b);
print(a > b);
print(a < b);
print(a != b);
print(a == b);

# Assignment operator
x = 5;
print(x);

x = 3;
x += 5;
print(x);

x = 10;
x -= 4;
print(x);

x = 4;
x *= 4;
print(x);

x = 12;
x /= 10;
print(x);

x = 2;
x **= 5;
print(x);


# Logical operator
x = 5;
print(x > 3 and x < 10); # True

x = 2;
print(x > 3 or x < 4); # True

x = 5
print(not(x > 3 and x < 10)); # False

# Python Membership Operators

x = ["apple", "banana"];
print("banana" in x); # True

x = ["apple", "banana"];
print("pineapple" not in x); # True

# Identity : to check memory location
x = [1,2,3]
y = [1,2,3]
print(x is y); # False

x = 10
y = 10
print(x is y); # True

# Operator Precedence BODMAS(bracket(), )

print((5 + 5) - (6 - 3));
print(100 + 5 * 3);