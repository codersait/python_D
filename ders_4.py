"""Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract,
   The program should calculate and print out the result of the operation with the given numbers.
   If the user types in anything else, the program should print out nothing.
"""
''' Programming terminology
- A statement is a part of the program which executes something. It often, but not always, refers to a single command.
- A block is a group of consecutive statements that are at the same level in the structure of the program.
- An expression is a bit of code that results in a determined data type. 
- A function executes some functionality.
- Data type refers to the characteristics of any value present in the program. 
- Similarly to natural languages, the syntax of a programming language determines how the code of a program should be written. ex:if:
- Debugging: If the syntax of the program is correct but the program still doesn't function as intended, there is a bug in the program.
'''
# password and odd/even number
# Alternative branches using the elif statement
"""
Please write a program which asks for two integer numbers. The program should then print out whichever is greater. 
If the numbers are equal, the program should print a different message.
- Some examples of expected behaviour:
    Please type in the first number: 5
    Please type in another number: 3
    The greater number was: 5
"""
# Logical operators
# - Especially in programming, logical operators are often called Boolean operators.
# - You can combine conditions with the logical operators and and or.
#  - number >= 5 and number <= 8
#  - number < 5 or number > 8
# - Sometimes it is necessary to know if something is not true. The operator not negates a condition
#  - range of 5 to 8 excluded

# example1 - Grades and points
# example2 - FizzBuzz

# Nested conditionals
# - whether a number is above zero, and then whether it is odd or even:
# password = "pass.2022@@"
# entered_pass = input("Sifre girin: ")
# if entered_pass == password:
#     print("Hosgeldiniz...")
# else:
#     print("Oppsss...Tekrar deneyiniz")

# sayi = int(input("Lutfen bir sayi giriniz..."))
#
# if sayi % 2 == 0:
#     print("Cift sayi girdiniz..")
# else:
#     print("tek sayi girdiniz..")
#
# number1 = int(input("Please type in the first number: "))
# number2 = int(input("Please type in the second number: "))
#
# if number1 > number2:
#     print("The greater number was:",number1)
# elif number2 > number1:
#     print("The greater number was:", number2)
# else:
#     print("They are equal....")
#
# 15 yasindan buyuk ve Bay olmak --- 16 yas bayan
# 18 yasindan buyuk veya Bay olmak --- 20 yas bayan --- 1 bayan

"""

======== OR ===========
True or True ===> True
True or False ===> True
False or False ==> False
False or True ===> True
======== AND =============
True and True ===> True
True and False ===> False
False and True ===> False
False and False ===> False

"""

# 5ten buyuk ve 8 den kucuk sayilar --- 5,6,7,8

# number = int(input("enter a number: "))
# if number >= 5 and number <=8:
#    print(number)
# 5ten kucuk veya 8 den buyuk sayilar ---
# number = int(input("enter a number: "))
# if number < 5 or number > 8:
#    print(number)
# number = int(input("enter a number: "))
# if not (number >= 5 and number <= 8):
#    print(number)
# age = 20
# if age >= 18:
#     print()
#     print("adult")
#     x =

