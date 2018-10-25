# age = int(input("Please enter your age."))
#
# # if (age >=16 and age<=65):
# if 15 < age < 66:
#     print("Have a good day at office.")

name = input("Please enter your name:")
age = int(input("Hi {0}! Please enter your age:".format(name)))
if(18 <= age < 31):
    print("Enjoy your vacation.")
else:
    print("Please go to work!")