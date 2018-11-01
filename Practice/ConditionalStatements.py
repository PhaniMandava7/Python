if False:
    print('Condition was True')
else:
    print('False')

language = '.NET'
if language == 'Python':
    print('Language was Python')
elif language == 'Java':
    print("Language was Java")
else:
    print('Language was something else')


# Difference between 'is' and ==
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # --------> Content comparison
print(a is b)  # --------> Object comparison
print(id(a))
print(id(b))
print()
print()


b = a
print(a == b)
print(a is b)
print(id(a))
print(id(b))


# False values:
    # False.
    # None.
    # Zero of any numeric type.
    # Any empty sequence.
    # Any empty mapping.