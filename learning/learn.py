# Conditions in Python = 
# age = 29
# if (age>=18):
# print("you are eligible for vote")

# age = 50
# if(age>=50):print("you are eligible for pension")

#if else in python

#age = int(input("enter your age"))

#if (age>=50):
#print("you are eligible for pension")
#else
#print("you are not eligible for pension")

#Short hand property of Python
#marks = 4
#res="you are pass"if marks>=40 else"you are fail"

#print(res)
#print(if "result:{res}")


#age = 40
#if age <=12:
#print("child")
#elif age<=19:
#print("teenager")

#elif age <=35:
#print("young adult")
#else

#print("adult")

#Nested if in python

#age = 60
#if is member = false

#if age >=60
#if is member
#print("30% senior discount")
#else:
#print("20% senior discount")
#else:
#print("not eligible for a senior discount")

# Nested if condition in pyhton 

#age = 70
#is member = false
# if age>=60
# if is member
# print("30% senior discount") 
#else:
#print("20% senior discount")
#else:
#print("not eligible for senior discount")

#Ternary condition statement of python
#Asign a value based on a condition 
#age = 16
#s = adult if age>=18 else"minor"

#print(s)

#Match case statement in python
#number=3
#match number:
#case 1:
#print ("one")
#case 2|3
#print ("two or three")
#case_:
#print("other number") 


# name = input("please enter your name")

# prnit("enter your math marks")
# print("enter your hindi marks")
# print("enter your english marks")
# print("enter your science marks")
# print("enter your social science marks")





# name = input("Enter your name  = ")

# hindi = int(input("Enter your hindi markes = "))
# English = int(input("Enter your English marks = "))
# Maths = int(input("Enter your maths = "))
# Sci = int(input("Enter your sci marks = "))
# sst = int(input("Enter your sst marks = "))

# total = hindi+English+Maths+Sci+sst


# percentage = total/5
# print("you name is =",name ,"\n")
# print("your total marks is =",total,"\n")
# print("your total %age is ", percentage,"\n")


# if((percentage>=80 and percentage<=100)):
#     print("Grade A")
# elif((percentage>=60 and percentage<80)):
#     print("Grade B")
# elif((percentage>=40 and percentage<60)):
#     print("Grade C")
# else:
#     print("you are fail ")


# name = input("enter your name")
# math = int(input("enter your math marks ="))
# hindi = int(input("enter your hindi marks="))
# english = int(input("enter your english marks="))
# bussines = int(input("enter your bussines marks="))
# ecconomics = int(input("enter your ecconomics marks="))

# total = math+hindi+english+bussines+ecconomics

# percentage = total/5
# print("your name is =",name,"\n")
# print("your total marks is=",total,"\n")
# print("your total%age is",percentage,"\n")


# if ((percentage>=80 and percentage<=100)):
#     print("grade A")
# elif((percentage>=60 and percentage<=80)):
#     print("grade B")
# elif((percentage>=40 and percentage<=60)):
#     print("grade C")
# else:
#     print("you are fail ")



# Exercise 1: Print first 10 natural numbers using while loop

# num = 1
# while num <= 10:
#     print(num)
#     num += 1


# list = ["geeks", "for", "geeks"]
# length=len(list)
# print(length)
# for index in range(length):
#     print(list[index])



# list = ["ram", "suresh", "mohan"]
# for index in range(len(list)):
#     print(list[index])
# else:
#     print("Inside Else Block")


# loop inside loop is known as nested loop 
# for iterator_var in sequence:   # outer loop
#    for iterator_var in sequence:  # inner loop 
#        statements(s)
#    statements(s)



# while expression:
#    while expression: 
#        statement(s)
#    statement(s)

# i=5
# for j in range(i):
#     print(j)



# for i in range(1, 5):
#     for j in range(i):
#         print(i, end=' ')
#     print()
# abc = 'geeksforgeeks'
# for letter in abc:
#     if letter == 'e' or letter == 's':
#         continue
#     print('Current Letter :', letter)


# for letter in 'geeksforgeeks':
#     if letter == 'f' or letter == 'o':
#         break

# print('Current Letter :', letter)

# for letter in 'geeksforgeeks':
#     pass
# print('Last Letter :', letter)

# fruits = ["apple", "orange", "kiwi"]

# for fruit in fruits:

#     print(fruit)


#print first 10 natural number using while loop


#i = 1
#while i <= 10:
  #  print(i)
  #  i += 1



  #calculate sum of all number from 1 to a given nummber 

#s  = 0
#n = int(input ("enter number"))

#for i in range (1,n+1,1):
 #   s += i
  #  print("\n")
   # print("sum is:",s)

  # print multiplication table of a given number 

#n = 4
#for i in range(1,11,1):
 #   product = n * i
  #  print(product)

# DISPLAY NUMBER FROM A LIST USING A LOOP

# number = [12,75,150,180,145,525,50]

# for item in number:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     elif item == 0:
#      print(item)
  



#numbers = [12, 75, 150, 180, 145, 525, 50]
# iterate each item of a list
#for item in numbers:
 #   if item > 500:
  #      break
   # elif item > 150:
    #    continue
    # check if number is divisible by 5
    #elif item % 5 == 0:
     #   print(item)



#COUNT THE TOTAL NUMBER OF DIGITS IN A NUMBER

#num = 75869
#count = 0
#while num != 0:
    # floor division
    # to reduce the last digit from number
 #   num = num // 10

    # increment counter by 1
  #  count = count + 1
#print("Total digits are:", count)


#PRINT THE FOLLOWING PATTERN




#h = 6
#g = 6
#for i in range(0,h+1):
 #   for j in range(g-i,0,-1):
  #      print(j,end ='')
   #     print()


   #COUNT THE TOTAL NUMBER OF DIGITS IN A NUMBER 

# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10

#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)




