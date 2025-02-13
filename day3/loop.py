
# Loop 2 types(for and while loop)

# using for loop 
for i in range(6):
    print(i)
    
   
# Using while loop 
i = 1;
while i < 6:
    print(i)
    i += 1;

### break statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
 
i = 1;
while i <= 5:
    print("Hello")
    i += 1;
    
    
for i in range(10):
    print("Sujan Magar");

x = "SUJAN"
for i in x:
    print(i)
    
##### While loop practice questions

# print 1 to 100
i = 1;
while i <= 100:
    print(i);
    i += 1
    
    
# Print from 100 to 1
i = 100;
while i >= 1:
    print(i)
    i -= 1;
   
# print the folowing list:
list = [1,4,9,16,36,49,64, 81, 100] 
i = 0;
while i < len(list):
    print(list[i])
    i += 1;
    
# to print the multiplication of number n
n = int(input("ENter number : "))
i = 1;
while i <= 10:
    print(n * i);
    i += 1;

#### to search x in this tuple
tup = (1,4,9,16,36,49,64, 81, 100);
num = int(input("Enter the number :"))
idx = 0
while idx < len(tup):
    if(num == tup[idx]):
        print("The searched value is:", num)
        break
    idx += 1;
    
## Break and continue

num = 0
while num < 10:
    print(num)
    if(num == 5):
        break
    num += 1
print("End of loop")


i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    
    i += 1;
    
    
    