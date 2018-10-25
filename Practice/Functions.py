def hello_func():
    pass


print(hello_func)   # -----> Returns the memory location where the function is stored.
print(hello_func())

print()
print()

def hello_func():
    print("Hello Function!")

hello_func()
print()
print()

def hello_func():
    return 'Hello Function!'

print(hello_func())
print()
print()


def hello_func(greeting):
    return '{} Function!'.format(greeting)
print(hello_func('Hey'))
print()
print()

def hello_func(greeting, name='Phani'):   #-----> Sets default value for parameter
    return '{} {}'.format(greeting,name)
print(hello_func('Hi'))
print(hello_func('Hello','Kumar'))
print(hello_func(name='Mandava',greeting='Hello'))
print()
print()


month_days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
def is_leap(year):
    return year%4==0 and (year%100!=0 or year%400==0)
def days_in_month(year,month):
    if month<1 or month>12:
        return 'Invalid month'
    elif month==2 and is_leap(year):
        return 29
    else:
        return month_days[month]

print(is_leap(2000))
print(is_leap(2017))
print(is_leap(1900))
print(days_in_month(2018,2))
print(days_in_month(2000,2))
print(days_in_month(2018,8))

print()
print()

def list_sum(*args):
    total = 0
    for num in args:
        total+=num*2
    return total


print(list_sum(2, 3, 4,5))


print()
print()

# args are variable number of arguments
# kwargs are variable number of 'key' arguments..
# Key arguments would be in 'key=value' form. Keys can be string without '' and cannot be numbers
def argsTest(required, *args, **kwargs):
    print(required)
    if(args):
        print('args->',args)
    if(kwargs):
        print('kwargs->',kwargs)

print()
print()
argsTest('Test',{'a':'Phani', 'b':'Kumar'})   # ---> takes the dictionary as one of the args.
argsTest('Test', a='Phani', b='Kumar' )       # ---> Here a,b are key words arguments.
argsTest('Test', {'a':'Phani', 'b':'Kumar'}, 'TestPostitionalArgument', a='Phani', b='Kumar' )

##########################################################
##------------Usecase for args, kwargs----------------####

# We can write some wrapper functions for our main functions and can modify our args/kwargs before calling the main function.
# Example:

def foo(required, *args, **kwargs):
    kwargs['name'] = 'main'
    new_args = args + ('extra',)
    bar(required,new_args, kwargs)

def bar(required, *args, **kwargs):
    print(required)
    if(args):
        print('args->',args)
    if(kwargs):
        print('kwargs->',kwargs)


