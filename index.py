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
# b = 5
# c = a==b
# print(c)



# dictionary in python 

# initialize empty dictionary
# d = {}
# print(d)

# d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
# print(d)

# # creating dictionary using dict() constructor
# d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# print(d1)



# d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# # Accessing an element using key
# print(d['name']) #For

# # Accessing a element using get
# print(d.get(3))  #Geeks



# ✔
# condition in python 

# age = 29
# if(age>=18):
#     print("you are eligible for vote")
    

# age = 50
# if(age>=50): print("you are eligible for pension")


# if else in python 

# age = int(input("Enter your age "))

# if(age>=50):
#     print("you are eligible for pension ")
# else:
#     print("you are not eligible for pension ")

# short hand property of python 
# marks = 4
# res = "you are pass" if marks >= 40 else "you are Fail"

# # print(res)
# print(f"Result: {res}")


# age = 40

# if age <= 12:
#     print("Child.")
# elif age <= 19:
#     print("Teenager.")
# elif age <= 35:
#     print("Young adult.")
# else:
#     print("Adult.")

# nested if in python 

# age = 60
# is_member = False

# if age >= 60:
#     if is_member:
#         print("30% senior discount!")
#     else:
#         print("20% senior discount.")
# else:
#     print("Not eligible for a senior discount.")

# nested if condition in python 

# age = 70
# is_member = False

# if age >= 60:
#     if is_member:
#         print("30% senior discount!")
#     else:
#         print("20% senior discount.")
# else:
#     print("Not eligible for a senior discount.")


# Ternary Conditional Statement in Python
# Assign a value based on a condition
# age = 16
# s = "Adult" if age >= 18 else "Minor"

# print(s)

# Match-Case Statement in Python

# number = 3

# match number:
#     case 1:
#         print("One")
#     case 2 | 3:
#         print("Two or Three")
#     case _:
#         print("Other number")



# loop in python

# while loop

# num =0
# while(num<10):
#     num = num+5
#     print("hello Good morning everyone ",num)

# cnt = 0
# while(cnt < 3):
#     cnt = cnt + 1
#     print("Hello Geek",cnt)
# else:
#     print("In Else Block")



# count = 0
# while (count == 0):
#     print("Hello Geek")




# Ram = 0
# while (Ram < 3):
#     Ram = Ram + 1
#     print(Ram, "Hey Ram ")
# else:
#     print("In Else Block")




# count = 0
# while (count == 0):
#     print("Hello Geek")


# for loop in python 

# n = 11
# for i in range(1,n):
#     print(i)


# li = ["Ram", "mohan", "rohan"]
# for i in li:
#     print(i)
    
# tup = ("pooja", "neha", "mukul")
# for i in tup:
#     print(i)
    
# s = "Geeks"
# for i in s:
#     print(i)
    
# d = dict({'x':123, 'y':354})
# for i in d:
#     print("%s  %d" % (i, d[i]))
    
# set1 = {1, 2, 3, 4, 5, 6}
# for i in set1:
#     print(i)

 
# number = int(input("Enter any number "))
# for i in range(1,11):
#     total = number*i
#     print(total)
    
    

    # function in python 
# A simple Python function
# def aman():
#     print("Hello everyone we are learners ")

# function calling 
# aman()

# functions with parameters 
# def add(num1: int, num2: int) -> int:
#     """Add two numbers"""
#     num3 = num1 + num2

#     return num3

# # Driver code
# num1=5
# num2=15
# num1, num2 = 5, 15
# ans = add(num1, num2)
# print(f"The addition of {num1} and {num2} results {ans}.")


# def aman(num1,num2):
#     print("hello everyone we are learners")
# aman(10,20)


# def aman(a,b):
#     c=a+b
#     print(c)
# num1=30
# num2=40
# x,y=30,50
# aman(x,y)
# aman(200,300)
# aman(num1,num2)

# Default Arguments
# Python program to demonstrate
# default arguments
# def myFun(x=50, y=50):
#     print("x: ", x)
#     print("y: ", y)


# # Driver code (We call myFun() with only
# # argument)
# myFun()
# myFun(100,200)



# A simple Python function to check
# whether x is even or odd
# def evenOdd(x):
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# # Driver code to call the function
# evenOdd(2)
# evenOdd(3)




# Python program to demonstrate
# default arguments
# def myFun(x=500, y=50):
#     print("x: ", x)
#     print("y: ", y)


# # Driver code (We call myFun() with only
# # argument)
# myFun(10,100)
# myFun()


# Python program to demonstrate Keyword Arguments
# def student(firstname, lastname):
#     print(firstname, lastname)


# # Keyword arguments
# # student(firstname='Geeks', lastname='Practice')
# lastname='Practice'
# firstname='Geeks'
# student(lastname,firstname)


# positional arguments 

# def nameAge(name, age):
#     print("Hi, I am", name)
#     print("My age is ", age)


# # You will get correct output because 
# # argument is given in order
# print("Case-1:")
# nameAge("Suraj", 27)
# # You will get incorrect output because
# # argument is not in order
# print("\nCase-2:")
# nameAge(27, "Suraj")

# arbitrary keyword arguments 
# Python program to illustrate
# *args for variable number of arguments
# def myFun(*argv):
#     for xyz in argv:
#         print(xyz)


# myFun('Hello', 'Welcome', 'to', 'letslearncoding')



# Python program to illustrate
# *kwargs for variable number of keyword arguments


# def myFun(**kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))


# # Driver code
# myFun(first='Geeks', mid='for', last='Geeks')


# A simple Python function to check
# whether x is even or odd


# def evenOdd(x):
#     """Function to check if the number is even or odd"""
    
#     if (x % 2 == 0):
#         print("even")
#     else:
#         print("odd")


# # Driver code to call the function
# print(evenOdd(4).__doc__)


# function within function 
# Python program to
# demonstrate accessing of
# variables of nested functions



# def f1():
#     s = 'I love xyz'
    
#     def f2():
      
#         print(s)
        
#     f2()

# # Driver's code
# f1()



# Anonymous Functions in Python

# Python code to illustrate the cube of a number
# using lambda function
# def cube(x): return x*x*x

# cube_v2 = lambda x : x*x*x

# # print(cube(2))
# print(cube_v2(3))

# Recursive Functions in Python

# def factorial(n):
#     if n == 0:  
#         return 1
#     else:
#         return n * factorial(n - 1) 
      
# print(factorial(4))


# Return Statement in Python Function


# def square_value(num):
#     """This function returns the square
#     value of the entered number"""
#     return num**2


# print(square_value(2))
# print(square_value(-4))


# Here x is a new reference to same list lst
# def myFun(x):
#     x[0] = 20


# # Driver Code (Note that lst is modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)



# def myFun(x):

#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#      x[0]= [20]


# # Driver Code (Note that lst is not modified
# # after function call.
# lst = [10, 11, 12, 13, 14, 15]
# myFun(lst)
# print(lst)



# def myFun(x):

#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = 20
#     print(x)


# # Driver Code (Note that x is not modified
# # after function call.
# x = 10
# myFun(x)
# print(x)


