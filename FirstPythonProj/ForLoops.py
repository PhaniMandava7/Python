# For print() statements, we can use paramater end='' to not to end the print in new line

number = "9,123,456,789,123,456,789"
cleanedNumber = ''
for i in range(0, len(number)):
    if number[i] in "0123456789":  # This would clear the ',' characters
        cleanedNumber = cleanedNumber + number[i]
newNumber = int(cleanedNumber)
print(newNumber)

cleanedNumber = ''
for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char
newNumber = int(cleanedNumber)
print(newNumber)
print()

# #Range(startIndex, endIndex, stepOf)
# # startIndex-inclusive,   endIndex-exclusive
# for i in range (0,101,5):
#     print(i)


for i in range(1, 11):
    print("{}th table:".format(i))
    for j in range(1, 21):
        print("{:2}*{:2} is {:4}".format(i, j, i * j))
    print('***********')
