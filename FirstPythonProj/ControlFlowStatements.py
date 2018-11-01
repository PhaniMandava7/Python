# for i in range(1, 11):
#     print("No is {:2} and squared is {:4} and cubed is {:4}".format(i, i ** 2, i ** 3))
#
# name = input("Please enter your name: ")
# age = int(input("Hi {}. Please enter your age: ".format(name)))
# if age >= 18:
#     print("You are old enough to vote.")
# else:
#     print("You are not  old enough to cast your vote. "
#           "Please comeback in {} years.".format(18-age))

print("Please guess a number:")
number = int(input())

# if number < 5:
#     print("Please select higher")
#     number = int(input())
#     if number == 5:
#         print("Your guess is right.")
#     else:
#         print("Sorry. Your guess is wrong.")
# elif number > 5:
#     print("Please select lower.")
#     number = int(input())
#     if number == 5:
#         print("Your guess is right.")
#     else:
#         print("Sorry. Your guess is not right.")
# else:
#     print("You got it first time.")


if number != 5:
    if number < 5:
        print("Please enter higher")
    else:
        print("Please enter lower")
    number = int(input())
    if number == 5:
        print("Your guess is right.")
    else:
        print("Sorry. Your guess is not right.")
else:
    print("You got it first time.")