even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]

even.append(12)
print(even)
numbers = even + odd
print(numbers)

# The below line adds elements of odd to even, and returns nothing.
# numbers = even.extend(odd)

# print(numbers)
# print(numbers.sort())
#
# numbers.append(11)
# numbers_in_orders = sorted(numbers)
# print(numbers_in_orders)
#
# numbers_in_orders.insert(19,13)
# print(numbers_in_orders)
# print(len(numbers_in_orders))


lists = [2, 4, 6, 8]
another_lists = lists

lists2 = list(lists)
lists2.append(11)
print('lists is another_lists ' + str(lists is another_lists))
print('lists2 equals another_lists ' + str(lists == another_lists))
print('lists is lists2s ' + str(lists is lists2))
print('lists equals lists2s ' + str(lists == lists2))
print()
print()


menu = []
menu.append(['egg', 'spam', 'bacon'])
menu.append(['egg', 'sausage','bacon'])
menu.append(['egg', 'spam'])
menu.append(['egg', 'bacon', 'spam'])
menu.append(['egg', 'bacon', 'sausage', 'spam'])
menu.append(['spam', 'bacon', 'sausage', 'spam'])
menu.append(['spam','egg','spam','spam','bacon','spam'])
menu.append(['spam', 'egg', 'sausage', 'spam'])

for meal in menu:
    if not 'spam' in meal:
        print(meal)
        for ingredient in meal:
            print(ingredient)


string = '1234567890'
my_iterator = iter(string)
print(next(my_iterator))



my_first_tuple = (1,2,3,4)
my_list = list(my_first_tuple)
print(my_list)

a, b, c, d = my_list
print(a, b, c, d)

my_second_tuple = (
    (1,2), (3,4), (5,6)
)
my_second_list = list(my_second_tuple)
print(my_second_list)

