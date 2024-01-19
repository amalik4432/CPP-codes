# name = "Tony Stark"
# age = 51
# is_genius = True

# name = input("Your Name: ")
# print("His name is " + name)


# age = input("Your age: ")
# print("age is " + str(int(age) + 2))


# age = input("Your age: ")
# print(int(age) + 2)



# Sum of two numbers

# first = input("Enter first number ") 
# second = input("Enter second number ")
# sum = int(first) + int(second)
# print(sum)

# Calculator

# first = input("Enter 1st number: ")
# second = input("Enter 2nd number: ")
# operaror = input("Enter +,-,*,/")

#thses numbers can also be converted below instead of in print

# int(first)
# int(second)

# if operaror == "+":
#     print(first + second )
# elif operaror == "-":
#     print(first - second )
# elif operaror == "*":
#     print(first * second )
# elif operaror == "/":
#     print(float(first) / float(second) )
# else:
#     print("Invalid Operator")

# a ="This will\'execute'"
# print(a)

# fruit = "mango"
# mangolen = len(fruit)
# print("mango length is",mangolen)
# print(fruit[0:5]) #include 0 not 5
# print(fruit[0:4]) #include 0 not 4
#  print(fruit[-4:-2]) 

# nm = "Harry"
# print(nm[-4:-2])

# a = "harry!!!!!!!"
# b = "harry"
# print(len(a)) 
# print(a.strip("!")) # remove !!!!
# print(a.upper()) # upper
# print(a.lower()) # lower
# print(a.rstrip("!")) # remove !!!!
# print(a.replace("harry", "john"))
# print(a.split(" "))

# head = "intro to ijs"
# print(head.capitalize())

# print(head.center(50))

# print(head.count("i"))

# print(head.endswith("s"))
# print(head.endswith("o", 3,5))
# print(head.endswith("s", 3,5))

# print(head.find("it"))
# print(head.isalnum())
# print(b.isalnum()) # a-z,0-9 only
# print(b.isalpha()) #only A-Z

# print(b.isdigit()) #only 0-9
# print(b.islower())
# print(b.isupper())
# print(b.isprintable()) 

# c = "\n"
# print(c.isprintable()) #not printable

# d ="            "
# print(d.isspace()) #only true if white spaces are present

# e = "World Health Organization"
# print(e.istitle())

# print(e.startswith("W"))

# print(e.swapcase)

# e = "world health organization"
# print(e.title()) #capital first words as title

#program check numbwer

# num = int(input("Enter a Number: "))
# if num > 0:
#     print("Number",num , "is positive")
# elif num < 0:
#     print("Number",num , "is negativw")
# else:
#     print("Number",num , "is zero")


# number = int(input("Enter a number: "))
# print("Your number is: ", number)
# if number < 0:
#     print("number is negative")
# elif number > 0:
#     if number <= 10:
#         print("Number is in between 1 to 10")
#     elif number  > 10 and number<= 20:
#         print("Number is in between 11 to 20")
#     else:
#         print("Number is greater than 20")   
# else:
#     print("The number is Zero")


#case statement program

# x = int(input("Enter a number: "))
# y = int(input("Enter a number: "))
# z = input("Enter a operator: ")
# match z:
#     case '+':
#         result = x+y
#         print(result)
#     case '-':
#         result = x-y
#         print(result)
#     case '*':
#         result = x*y
#         print(result)
#     case '/':
#         result = x/y
#         print(result)
#     case _:
#         print("invalid choice")


# name = "kashaf"
# for i in name:
#     print(i,"\n")

#table

# x = int(input("Enter a number: "))
# for i in range(10):
#     print(x, "x", i+1 ,"=",x*(i+1))

# for k in range(1,15,2):
#     print(k)
# a ="gggg"

# x = int(input("Enter a number"))
# i = 1
# while i<= 10:
#     print(x, "*", i, "=", x*i )
#     i += 1 

# def table(x):
#     i = 1
#     while i<= 10:
#      print(x, "*", i, "=", x*i )
#      i += 1 
# x = int(input("Enter a number"))
# table(x)



