
# print(help(dict))

my_dict = {1 : 'one', 2 : 'two', 3 : 'three'}
print(my_dict)
print(my_dict.items())
print()
print()

# print(my_dict[4])  # ----------->>> Throws KeyError
print(my_dict.get(4))  # ------->>> Returns None
print(my_dict.get(4, "Not found"))   # --------->>> Returns 'Not found' if no element
print()
print()


print(my_dict.update( { 1: 'ONE' , 3 : 'THREE' , 4 : 'FOUR'} ))  # ------------>>> Updates Dictionary
print(my_dict.popitem())
print(my_dict)
print()
print()

# del my_dict[4]


print(my_dict.pop(23, "No value"))
print(my_dict)
print(my_dict.pop(1, "no value"))
print(my_dict)
print()
print()

print(my_dict.keys())
print()
print()
print()

for key, value in my_dict.items():
    print(key, '->', value)

print('Test')
for keys in my_dict.keys():
    print(key, '->', my_dict[key])