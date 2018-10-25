person = {'name' : 'Phani', 'age' : 26}

# basic formatting
sentence = 'My name is {} and I am {} years old'.format(person['name'], person['age'])
print(sentence)


sentence = 'My name is {name} and I am {age} years old'.format(name='Phani', age=26)
print(sentence)

# formatting with numbers. this is useful when we have to use variables multiple times
sentence = 'My name is {0} and I am {1} years old'.format(person['name'], person['age'])
print(sentence)


# ======>>>> Unpacking the dictionary
sentence = 'My name is {name} and I am {age} years old and five years ago, my age was {age}-5 years'.format(**person)
print(sentence)


tag = 'h1'
text = 'This is a heading'
sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

sentence = 'My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence)

l = ['Phani', 26]
sentence = 'My name is {0[0]} and I am {0[1]} yeards old'.format(l)
print(sentence)
print()


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Phani', 26)

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)



# =========>>>>>>> Formatting numbers <<<<<<==============
for i in range(0,11):
    sentence = 'The value is {}'.format(i)
    print(sentence)

for i in range(11):
    sentence = 'The value is {:02}'.format(i)
    print(sentence)

sentence = '1 MB is equal to {:,} bytes'.format(1000**2)
print(sentence)

sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
print(sentence)

for i in range(11):
    sentence = 'The value is {:f}'.format(i)
    print(sentence)


for i in range(0,11):
    sentence = 'The value is {:.2f}'.format(i)
    print(sentence)
print()
print()


pi = 3.1415932834
sentence = 'Pi value is {:.4f}'.format(pi)
print(sentence)



# =========>>>>>>> Formatting Dates <<<<<<<<=============
import datetime
my_date = datetime.datetime(2018, 8, 7, 3, 12, 35)
print(my_date)

sentence = '{:%B %d, %Y }'.format(my_date)
print(sentence)

sentence = '{0:%B %d, %Y} fell on {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)