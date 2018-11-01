
string = '1234567890'

# iter(iterableObject) method returns an iterator for the specified iterable object.
my_iterator = iter(string)

# next(iterator) returns next element in the iterator.
print(next(my_iterator))
print()

for char in string:
    print(char)
print()

for char in my_iterator:
    print(char)
print()

string = '1234567890'
iterator = iter(string)
for i in range(0,len(string)):
    print(next(iterator))

