print('Hello World')
print("Hello World!")
print(5)

# name = input("Enter your name:\a")
# print('Hello ' + name)

# Problem-1
# result = ''
# for i  in range(2000, 3001):
#     if(i%7==0 and i%5!=0):
#         result = result + ',' + str(i)
# print(result)
# print()
# print()


# Problem-2
# number=int(input('Please enter a number:'))
# result=1
# for i in range(1,number+1):
#     result = result*i
# print("Factorial is: \t", result)
#
#
# def fact(x):
#     if x==0:
#         return 1
#     return x * fact(x-1)
#
# print("Factorial from function:\t", fact(number))
# print()
# print()


# Problem-3
# dic = {}
# number=int(input('Please enter a number:'))
# for i in range(1, number+1):
#     dic[i] = i*i
# print(dic)
# print()
# print()


# Problem-4
# numbers_string = input('Please enter numbers separated by \',\': \a')
# numbers_list = numbers_string.split(',')
# numbers_tuple = tuple(numbers_list)
# print(numbers_list)
# print(numbers_tuple)
# print()
# print()


# Problem-6
# import math
#
# numbers = input('Please enter the numbers separated by \',\': \a')
# numbers_list = numbers.split(',')
# var_c = 50
# var_h = 30
# result = []
# for d in numbers_list:
#     result.append(round(math.sqrt((2* var_c * int(d)) / var_h)))
#
# for index, r in enumerate(result, 1):
#     print(index , '->', r)
# print()
# print()


# Problem-7 ------------------------> Not Completed
# indices = input('Please enter 2 numbers separated by \',\': \a')
# indices_list = indices.split(',')
# for i in indices_list:
#     indices_list[i] = int(indices_list[i])
#
# for i in range(indices_list[0]):
#     for j in range(indices_list[1]):
#         print(i * j, '  ')


# Problem-8
# words_seq = input("Please enter sequence of words separated by \',\': \a")
# words = words_seq.split(',')
# words.sort()
# print(','.join(words))


# Problem-9
# lines = []
# print('Please type in the lines. If done, press Enter')
# while True:
#     s = input()
#     if s:
#         lines.append(s.upper())
#     else :
#         break
# for line in lines:
#     print(line)


# Problem-10
words_seq = input('Please enter words separated by \' \': \a')
words = words_seq.split(' ')
sorted_words = sorted(list(set(words)))
print(' '.join(sorted_words))