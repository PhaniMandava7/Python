parrot = "Norwegian Blue"
print(parrot) #Norwegian Blue
print(parrot[0]) #N
print(parrot[13]) #e
# print(parrot[14]) --> throws erros
print(parrot[-1]) #e
print(parrot[-14]) #N

# identifier[startIdex : endIndex] --> Slice
# startIndex-inclusive, endIndex-exclusive.
print(parrot[10:14])
print(parrot[-4:])  # To print till the end of the line, we don't have to specify endIndex.

#identifier[start: end : stepsOf]
print(parrot[0 : 6 : 2]) #Nre

number = "9,123,123,345,456,567,678,789"
print(number[1 : : 4])

numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0 : : 3])

print("Hello " * 4)

today = "sunday"
print("sun" in today)


#***********String Formatting***********

#String concatinating with integer.
age = 25
print("My age is " + str(age) + " years")
years4 = 4

#with replacement fields.
print("My age is {0} years. After {1} years it will be {2}"
      .format(age, years4, age+years4))
for i in range(1,11):
    print("No is {0:2}, squared is {1:4}, cubed is {2:4}".format(i, i**2, i**3))
print()
print()
for i in range(1,11):
    print("No is {0:2}, squared is {1:<4}, cubed is {2:<4}".format(i, i**2, i**3))
print()
print("PI value is approximately {0:12.50}".format(22/7))

#with formatting operators.
print("My age is %d years. After %d years, it will be %d"
      % (age,years4,(age+years4)))
print("My age is %d %s and %d %s." % (age, "years", 11, "months"))

for i in range(1,11):
    print("No is %2d, squared is %4d, cubed is %4d" %(i, i**2, i**3))
print()
print()

print("PI value is %12.50f" %(22/7))

if 1 not in range(10,199):
    print("Not in range")