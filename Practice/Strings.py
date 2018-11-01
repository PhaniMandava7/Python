message='Hello World'
print(message)
print(message[0])
print()

print(message[0:])
print(message[0:5])
print(message[6:11])
print(message[6:])
print()

print(message[::-1])
print(message[10:6:-1])
print(message[0:10:2])
print(message[10:0:-2])
print()

print(len(message))
print(message.lower())
print(message.upper())
print(len(message))
print(message.count('l'))
print(message.count('z'))
print(message.find('World'))
print(message.find('world'))
print(message.replace(' ', ','))        # replaces and returns a string.
print(message)
print()

greeting='Hello'
name='World'
message=greeting + ' ' + name
print(message)
print(message.startswith('H'))

message = '{}, {}. Welcome'.format(greeting, name)
print(message)
message = f'{greeting}, {name}. Welcome'    # works with Pyton 3.6 or higher
print(message)
print(f'{greeting}, {name.upper()}. Welcome')
print(message.istitle())
print(message.swapcase())
print(message.expandtabs(100))


# print(help(int))
testNum = 10
print(testNum.__ge__(34))
print(testNum.__sizeof__())
print(testNum.__or__(35))


nums_List = [0,1,2,3,4,5,6,7,8,9]
print(nums_List[-1:-8:-2])
print(nums_List[-9:-1:2])
print()
print()


test_string = "Test String"
print(test_string.casefold())

print(help(str))
print(test_string.ljust(20,'*'))
print(test_string.rjust(20,'*'))

test_string= "        Test String        "
print(test_string.lstrip())
print(test_string.rstrip())
print()