print(range(-1,10))

list1 = list(range(-2,10))
print(list1)

even = list(range(-10,10,2))
odd = list(range(-9,10,2))
print(even)

my_range = range(1, 100 ,2)

# indexing can be done on ranges.
print(my_range[40])

my_range = range(1,1000000,2)
print(my_range[500])

# sevens = range(7, 10000, 7)
# user_input = int(input("Please enter a number between 0 and 10000:"))
# if user_input in sevens:
#     print("{} is divisible by seven.".format(user_input))
# else:
#     print("{} is not divisible by seven.".format(user_input))
#


decimals = range(0,100)
my_range = decimals[3:40:3]
print(my_range == range(3,40,3))


print(range(0,5,2) == range(0,6,2))
print(range(0,5,2) is range(0,6,2))


my_decimals = range(1,10)
#Negative slicing works as max_index-2(in this case, 100-2=98 would yield the value of 99)
for i in my_decimals[::-2]:
    print(i)

#To specify negatives in stepping, we have to reverse the positions of start & end indices.
for i in range(9, 0, -2):
    print(i)


for i in range(0, 100 , -2):
    #This yields nothing as we start from o, adding -2 would never reach 100.
    print(i)


string = ".egaugnal lufrewop yrev si nohtyP"
backString = string[::-1]
print(backString)