# Tuples are similar to Lists, but the difference is Tuples are immutable.
empty_tuple = ()
empty_tuple = tuple()

tuple_1 = ('History', 'Math', 'Physics')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[0] = 'Arts'
print(tuple_1)
print(tuple_2)

print(tuple_1[0:2])
print()

print(help(tuple))