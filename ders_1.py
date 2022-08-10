# commands
# A program of multiple commands
"""
Welcome to Introduction to Programming!
First we will practice using the print command.
This program prints three lines of text on the screen.
"""
# Arithmetic operations
# Commenting
# Information from the user
# Naming variables
# String Concatenation
# More than one input / name,email
# variable_name = ... / ... means the value stored in the variable.
# Changing the value of a variable
# Choosing a good name for a variable
# A variable name should begin with a letter, and it can only contain letters, numbers and underscores _.
# Integers
# Printing with f-strings
# Floating point numbers -- calculate mean
# calculate bmi--- weight/(height/100)**2
# Numbers as input -- Yas hesapla
# calculate bmi with input
# Please write a program which asks the user for four numbers. The program then prints out the sum and the mean of the numbers.
# Boolean values and Boolean expressions
# Comparison operators
# Indentation -- You can use the Tab key
# # Python recognises that a block of code is part of a conditional statement if each line of code in the block is indented the same.
'''Please write a program which asks the user for two numbers and an operation. If the operation is add, multiply or subtract, 
   The program should calculate and print out the result of the operation with the given numbers. 
   If the user types in anything else, the program should print out nothing.
'''
''' Programming terminology
- A statement is a part of the program which executes something. It often, but not always, refers to a single command.
- A block is a group of consecutive statements that are at the same level in the structure of the program.
- An expression is a bit of code that results in a determined data type. 
- A function executes some functionality.
- Data type refers to the characteristics of any value present in the program. 
- Similarly to natural languages, the syntax of a programming language determines how the code of a program should be written. ex:if:
- Debugging: If the syntax of the program is correct but the program still doesn't function as intended, there is a bug in the program.
'''
# print(3 > 2)
# veri tipleri
#   text --- String -- str
#   number --- Integer, Floating Numbers
#   boolean  --- True, False
# convention
#
# dogum_yili = input("Yasiniz nedir: ")
# yas = yas hesapla
# print(yas)
# person_details = ""
# print("Benim adim "+first_name+" email adresim "+email)
# print(f"benim adim {first_name} email adresim {email}")

ondalik_sayi = int(input("ondalik sayi giriniz "))

print(10+10.4)
print(10+ondalik_sayi)
name = "furkan"
dogum_yili_tarih = 2000
# his name is furkan. He is 18 years old.

# print("his name is",name+".","He is ",age,"years old")
# sentence = "his name is "+name+". He is " + str(age)+ " years old"
f_sentence = f"his name is {name}. He is {2022 - dogum_yili} years old."
print(f_sentence)







