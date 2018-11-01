import os
# print(os.listdir('C:/Users/Phani/Desktop/OozieClientConnect.java'))

'''
f=open('C:/Users/Phani/Desktop/OozieClientConnect.java','r')
s =f.read()
stripped = s.split('\n')
for line in stripped:
    print(line)
f.close()
'''


with open('C:/Users/Phani/Desktop/OozieClientConnect.java','r') as f:
    f_contents = f.read()
    print(type(f_contents))
    f_stripped=f_contents.split('\n')
    print(type(f_stripped))
    print(f_contents)
    print('+++++++++++++++++++++++++++++++++')
    print(f_stripped[:5])

print('*****************************************')

with open('C:/Users/Phani/Desktop/OozieClientConnect.java','r') as f:
    f_contents = f.readline()
    print(type(f_contents))
    print(f_contents)

print('*****************************************')

with open('C:/Users/Phani/Desktop/OozieClientConnect.java','r') as f:
    f_contents = f.readlines()
    print(type(f_contents))
    print(f_contents[:5])

print('*****************************************')


# f.seek(n)    ------>> points to the nth position in the file.
# f.tell()     ------>> gives the current position in the file.

with open('C:/Users/Phani/Desktop/OozieClientConnect.java','r') as f:
    size_to_read=100
    f_contents=f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents,end='')
        f_contents=f.read(size_to_read)



print()
print()
print()




# For writing we have 2 modes: w and a
# 'w' mode overrides the content
# 'a' mode appends to the content
# If the file is not present, both modes will create a file

with open('C:/Users/Phani/Desktop/testFileFromPython.txt','w') as f:
    f.write('This is a test file from Python')




print()
print()


with open('C:/Users/Phani/Desktop/OozieClientConnect.java', 'r') as rf:
    with open('C:/Users/Phani/Desktop/testFileFromPython.txt','w') as wf:
        f_contents = rf.read()
        wf.write(f_contents)


with open('C:/Users/Phani/Desktop/OozieClientConnect.java', 'r') as rf:
    with open('C:/Users/Phani/Desktop/testFileFromPython.txt','w') as wf:
        for line in rf:
            wf.write(line)


with open('C:/Users/Phani/Desktop/OozieClientConnect.java', 'r') as rf:
    with open('C:/Users/Phani/Desktop/testFileFromPython.txt', 'w') as wf:
        f_contents = rf.read(100)

        while len(f_contents) > 0:
            wf.write(f_contents)
            f_contents = rf.read(100)

# -------------------------
# Copying image files
# -------------------------

with open('C:/Users/Phani/Desktop/DesktopImg.jpg','rb') as rf:
    with open('C:/Users/Phani/Desktop/DesktopImg2.jpg','wb') as wf:
        f_contents = rf.read(100)
        while len(f_contents)>0 :
            wf.write(f_contents)
            f_contents=rf.read(100)