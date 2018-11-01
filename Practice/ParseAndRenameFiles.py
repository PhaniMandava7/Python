import os
print(os.getcwd())
os.chdir('E:/WorkSpaces/IntelliJWS/PythonWS/Practice/testFolderForRenamingFiles')
for f in os.listdir('E:/WorkSpaces/IntelliJWS/PythonWS/Practice/testFolderForRenamingFiles'):
    f_name, f_ext=os.path.splitext(f)
    f_title, f_course, f_num =f_name.split('-')

    f_num=f_num.strip()[1:].zfill(2)
    f_title=f_title.strip()
    new_name='{}-{}{}'.format(f_num,f_title,f_ext)
    os.rename(f,new_name)