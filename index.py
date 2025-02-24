# print("hello everyone we are learners")



# num1 = int(input("Enter first number "))
# num2= int(input("Enter the second number "))

# num3 = num1+num2
# print(num3)



# num1 = int(input("Enter first number "))
# print(type(num1))

# num2 = input("Enter the second number ")
# print(type(num2))


# data types in python practical 




# hello hi kaise ho we are learning about data analytics development 

# print("hello world")

# print("hello world")



# Operators in python 

# arithmatic operator 
a = 5
b = 3
c=a+b
# print(f'the addition of a and b = {c}')

# print("The Addition of a and b =",c)


# Addition
# print("Addition:", a + b)  

# # Subtraction
# print("Subtraction:", a - b) 

# # Multiplication
# print("Multiplication:", a * b)  

# # Division
# print("Division:", a / b) 

# # Floor Division
# print("Floor Division:", a // b)  

# # Modulus
# print("Modulus:", a % b) 

# # Exponentiation
# print("Exponentiation:", a ** b) 


# Comparison of Python Operators

# a = 13
# b = 33

# print(a > b)
# print(a < b)
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)


# Logical Operators in Python
# a = True 
# b = False
# print(a and b)  
# print(a or b)
# print(not a)


# Bitwise Operators in Python

# Bitwise NOT
# Bitwise Shift
# Bitwise AND
# Bitwise XOR
# Bitwise OR

# a = 10
# b = 4

# print(a & b)
# print(a | b)
# print(~a)
# print(a ^ b)
# print(a >> 2)
# print(a << 2)



# Assignment Operators in Python

# a = 10
# b = a
# print(b)
# b += a
# print(b)
# b -= a
# print(b)
# b *= a
# print(b)
# b <<= a
# print(b)


# Identity Operators in Python
# is          True if the operands are identical 
# is not      True if the operands are not identical 

# a = 10
# b = 20
# c = a

# print(a is not b)
# print(a is c)

# Membership Operators in Python

# in            True if value is found in the sequence
# not in        True if value is not found in the sequence

# x = 24
# y = 20
# list = [10, 20, 30, 40, 50]

# if (x not in list):
#     print("x is NOT present in given list")
# else:
#     print("x is present in given list")

# if (y in list):
#     print("y is present in given list")
# else:
#     print("y is NOT present in given list")

















# 24/02/2025

# Python Data Types

# Python Data types are the classification or categorization of data items. It represents the kind of value that tells what operations can be performed on a particular data. Since everything is an object in Python programming, Python data types are classes and variables are instances (objects) of these classes. The following are the standard or built-in data types in Python:

# Numeric – int, float, complex
# Sequence Type – string, list, tuple
# Mapping Type – dict
# Boolean – bool
# Set Type – set, frozenset


# 1. Numeric Data Types in Python

#  int, float, string, list and tuple
# x = 50 #int
# print(x)
# print(type(x))
# x = 60.5 #float
# print(x)
# print(type(x))

# x = "Hello World" #string
# print(x)
# print(type(x))
# x = ["geeks", "for", "geeks"] #list
# print(x)
# print(type(x))
# x = ("geeks", "for", "ravi")  #tuple
# print(x)
# print(type(x))

# x = {"geeks", "for", "ravi"} #set
# print(x)
# print(type(x))



# 1. Numeric Data Types in Python
# a = 5
# print(type(a))
# print(a)


# b = 5.0
# print(type(b))
# print(b)

# c = (2 + 4j) 
# print(type(c))
# print(c)


# 2. Sequence Data Types in Python
# string 

# s = 'Welcome to the Geeks World'
# print(s)
# name = "hello my name is aman "
# print(name)

# # check data type 
# print(type(name))

#  string indexing always starts from zero 
# name2 = "Aman"
# name2[0]="R"  immutable =>which value can't be changed by using its indexing number 
# access string with index
# print(name2[0])
# print(name2[1])
# print(name2[2])
# print(name2[3])
# print(name2)


# list in python 
# Empty list
# a = []

# # list with int values
# a = [1, 2, 3]
# print(a[0])

# # list with mixed int and string
# b = ["Geeks", "For", "Geeks", 4, 5]
# print(b[0])

# a = ["Geeks", "For", "Geeks"]
# print("Accessing element from the list")
# print(a[0])
# print(a[2])

# print("Accessing element using negative indexing")
# print(a[-1])
# print(a[-3])


# Tuple Data Type

# initiate empty tuple
# t1 = ()

# t2 = ('Geeks', 'For')
# print("\nTuple with the use of String: ", t2)

# t1 = tuple([1, 2, 3, 4, 5])

# # access tuple items
# print(t1[0])
# print(t1[-1])
# print(t1[-3])

# 3. Boolean Data Type in Python

# a = 50
# b = 500
# c = a==b
# print(c)
