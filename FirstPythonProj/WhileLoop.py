# available_exits = ["east", "west", "north east"]
# chosen_exit = ""
#
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please enter an exit. To quit, type quit ")
#     if chosen_exit == 'quit':
#         print('Game Over')
#         break
# else:
#     print('You got out!')
# print()

# number = int(input('Please enter a number:'))
# chances = 1
# while (number != 5) | (chances < 3):
#     if chances ==3 :
#         print('sorry, you didn\'t get it.')
#         break
#     if number < 5:
#         number = int(input('Please enter higher'))
#     if number > 5:
#         number = int(input('Please enter lower'))
#     chances += 1
# else:
#     print("you got it")


import random

highest = int(input('Please enter the highest number'))
max_chances = int(input('Please enter the number of chances'))
chances = 0
number = random.randint(1, highest)
chosen_number = int(input('Please enter the number'))
chances += 1
while (chosen_number != number) | (chances < max_chances):
    if chances == max_chances:
        print("You have reached max chances.")
        break
    if chosen_number < number:
        chosen_number = int(input("Please enter higher."))
    if chosen_number > number:
        chosen_number = int(input("Please enter lower"))
    if chosen_number == number:
        print("You guessed it.")
    chances += 1

else:
    print("Number is {}".format(int(number)))
    print("You have guessed first time.")