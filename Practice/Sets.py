# Sets are collection of distinct elements with no ordering.
# Sets are good at membership testing.
# empty_set = {}  -------> this creates a dict.
empty_set = set()

courses_set = {'History', 'Physics', 'Math'}
print(courses_set)

courses_set.add('Math')
print(courses_set)

print('Math' in courses_set)


courses_set = {'History', 'Physics', 'Math'}
courses_set2 = {'History', 'Arts', 'Music'}
print(courses_set.intersection(courses_set2))
print(courses_set.difference(courses_set2))
# courses_set.difference_update(courses_set2)
# print(courses_set)
print(courses_set.union(courses_set2))