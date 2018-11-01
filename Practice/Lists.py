# Lists is the collection of items.
empty_list = []
empty_list = list()

courses = ['Test', 10]
print(courses)
courses = ['Math', 'Physics', 'Chemistry', 'CompScience']
print(courses)
print()

# print(help(list))
print(len(courses))
print()

print(courses[0])
print(courses[-1])
print(courses[-2])
print()

print(courses[0:2])
print(courses[:3])
print(courses[1:4])
print(courses[1:])
print(courses[::-1])
print(courses[3:0:-2])
print()

# Adding elements to List
courses.append('Arts')
print(courses)

# Adding element at specific location
courses.insert(3,'Music')
print(courses)

# Adding elements of another list
courses_2 = ['Programming', 'Spanish']
# courses.extend(courses)
# print(courses)
courses.extend(courses_2)
print(courses)
print()

# Remove elements
courses.remove('Programming')
print(courses)
removedCourse = courses.pop()
print(removedCourse + ' is removed from the list. Now the list is ' + str(courses))
print()


# Reverse
courses.reverse()    # in-place reverse
print(courses)

# Sorting
# iterable.sort() ----> In-place
# sorted(iterable) -----> not in-place
courses.sort()
print(courses)
print()

nums = [1,5,8,2,6,10]
nums.sort()
print(nums)
nums = [1,5,8,2,6,10]
nums.sort(reverse=True)
print(nums)

nums = [1,5,8,2,6,10]
print(sorted(nums))
print(sorted(nums, reverse=True))
print()

print(min(nums))
print(max(nums))
print(sum(nums))
print()

# Index of particular element
print(courses.index('Arts'))

# Checking if the particular element is in the list
print('Art' in courses)
print()

for course in courses:
    print('Course is ' + course)

for index, course in enumerate(courses):
    print(index, course)

print()

for index, course in enumerate(courses, start=1):
    print(index, course)

print()

iterItems = []
for course in courses:
    iterItems.append(course)
joinedIterElements = ','.join(iterItems)
print(joinedIterElements)

splittedCourses = joinedIterElements.split(',')
print(splittedCourses)

print()


# Objects are mutable
courses = ['History', 'Arts', 'Science', 'Engineering']
courses_2 = courses
print(courses)
print(courses_2)
courses_2[0] = 'Music'
print(courses)
print(courses_2)

print(help(list))