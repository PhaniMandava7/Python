import os
from datetime import datetime

# print(dir(os))
print(os.name)
print(os.getcwd())  # --> gets current working directory

os.chdir('E:/WorkSpaces/')   #   ---> changes the directory to the path specified
print(os.getcwd())

print(os.listdir())  #  ---> lists files,folders of current working directory.
print()
print(os.listdir('E:/'))  # ---> lists files,folders in the specified path
print()
print()

'''
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print('\tCurrent path:', dirpath)
    print('\tDirectories: ', dirnames)
    print('\tFiles: ', filenames)
    print()
'''
print()

print(os.environ)
print(os.environ.get('HADOOP_HOME'))
print()

os.rmdir('os_demo')   #  ---> deletes directory
os.removedirs('os_demo2/Sub-dir1')   # ---> removes directory and parent/child directories as well.

os.mkdir('OS_Demo')  #  ---> creates a directory
os.makedirs('OS_Demo2/Sub-dir1')  #  ---> creates directory and parent/child directories as well.
os.rename('OS_Demo', 'os_demo')
os.renames('OS_Demo2', 'os_demo2')
print(os.listdir(os.getcwd()))
print()
print()

print(os.stat('C:/Users/Phani/Desktop/exchange_chart.py'))
last_modified_time = os.stat('C:/Users/Phani/Desktop/exchange_chart.py').st_mtime
print(datetime.fromtimestamp(last_modified_time))
print()
print()

print(os.getcwd())
filePath = os.path.join(os.getcwd(), 'test.txt')  # -----> returns a string path with current directory appended with a test.txt
print(filePath)
print(os.path.basename('/tmp/phani/test.txt'))
print(os.path.dirname('/tmp/phani/test.txt'))
print(os.path.split('tmp/phani/test.txt'))
print(os.path.exists('/tmp/phani/test.txt'))