import sys
import my_module as mm

courses = ['Math', 'Science', 'Comp', 'French']
print(mm.find_index(courses, 'French'))
print(mm.find_index(courses, 'English'))

print('sys.version_info->',sys.version_info)
print('sys.api_version->',sys.api_version)
print('sys.exc_info()->',sys.exc_info())
print('sys.getprofile()->',sys.getprofile())
print('sys.modules->',sys.modules)
print('sys.path->',sys.path)