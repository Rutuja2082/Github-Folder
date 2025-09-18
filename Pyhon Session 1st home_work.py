
#print() Function 
#1
print("Hello world!")

#2.Q1: Print "Hello Rutuja" 5 times in a single line.
print(("Hellow Rutuja ")*5)

#3. Q2: Print the numbers 1 to 5 on the same line, separated by commas.
print(1,2,3,4,5, sep=",")
# (sep defines the separator between arguments.)

#4. Q3: Print a sentence but suppress the new line at the end.
print("Learning", end= " ")  #end=" " avoids line break.
print("Pyhton")           

# 5. Q4: Print a formatted string showing your name and location
name = "Rutuja"
location = "Dharashiv"
print(f"My name is {name} and I am from {location}.")

# if......else
if 1==2:
    print(1)
else:
    print(2)

#1.Q1: Check if a number is even or odd.
i = 3 
if i % 2 == 0:
    print("even")
else:
    print("odd")

#2. Check if a number is positive, negative, or zero.
i = -4
if i> 0:
    print("positive")
elif i < 0:
    print("negative")
else:
    print("zero")

#3.Find the largest of two numbers.
x, y = 12, 20
print("largest=", x if x > y else y)

#4
if 5<2:
    print("Five is greater than two")
print("another statement")

if 5 > 2:
    print("Five is greater than two")
print("another statement")

# Use of variable
i = 1
print(i)

# Swap two variables without using a third variable.
a, b = 2, 5
a, b = b, a
print(a, b)

#Asign a string to a variable and print its length.
text = "Python"
print(len(text))

a = 4
b = "Hello"
print(type(a), a)
print(type(b), b)

#Type casting

x = int(5)
y = str("Hello")
print(x)
print(y)
print(type(x))
print(type(y))

#Convert string to integer and add.
x = "10"
y = int(x) + 5
print(y)

price = 99.99
print(int(price))

rollno = 24
print("RollNo = "+ str(rollno))

# Manys  Values to Multiple Variables


a,b,c = 1,2,3
print("value of a =", a)
print("value of b =", b)
print("value of c =", c)

x, y, z = 1, 2, 3 
print(x + y + z)

# One value to multiple variables

a = b = c = "1234567"
print("value of a =", a)
print("value of b =", b)
print("value of c =", c)


#Multiple values to a variable 

Colors= "Red", "Orange", "Pink","Yellow"
print(Colors)
print(type(Colors))



