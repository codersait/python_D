# repetition, or iteration
# control structures
# conditional structures allow you to choose between sections of code
# iteration structures allow you to repeat sections of code.
# counter
# countdown
# password example
# - Loops and helper variables -- attemps
# Adding loops to programs also adds to the potential sources of bugs. It becomes even more important to master the
# use of debugging print statements
# Concatenating strings with the + operator
# count = 1
# while count < 11:
#     print("sait")
#     count += 1
count = 1
# while count != 6:
#     print("sait")
#     count = count + 1
# while True:
#     print("sait")
#     if count == 5:
#         break
#     count = count + 1
# countdown
# count = 10
#
# while count > 0:
#     print(count)
#     count = count - 1

password = "@@2022"

deneme = 0
while True:
    user_pass = input("Sifre giriniz: ")
    deneme = deneme + 1
    if user_pass == password:
        print("Hos geldiniz")
        break
    else:
        print("Tekrar deneyiniz")
    if deneme == 3:
        break

print("denemeler:",deneme)








