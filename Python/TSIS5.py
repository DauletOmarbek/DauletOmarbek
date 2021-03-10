import os
def Renama_directory():
    print("Old name of file?")
    a=str(input())
    print("New name of file?")
    b=str(input()) 
    print("Directory of file?")
    c=str(input()) 
    if os.path.exists(os.path.join(c,a)):
        old_file = os.path.join(c, a)
        new_file = os.path.join(c, b)
        os.rename(old_file, new_file)
    else:
        print("NO")
def Print_number_of_files():
    print("What is the way of the directory")
    b =str(input())
    if os.path.exists(b):
        c = len([name for name in os.listdir(b) if os.path.isfile(os.path.join(b, name))])
        print(c)
    else:
        print("NO")
def Print_number_of_directory():
    print("What is the way of the directory")
    b =str(input())
    if os.path.exists(b):
        c = len([name for name in os.listdir(b) if os.path.isdir(os.path.join(b, name))])
        print(c)
    else:
        print("NO")
def List_content_of_the_directory():
    print("What is the way of the directory")
    a=str(input())
    if os.path.exists(os.path.join(a)):
        print(sorted(os.listdir(a)))
    else:
        print("NO")
def Add_file_to_this_directory():
    print("Name of file?")
    a=str(input())
    print("What is the way of the directory")
    b=str(input())
    if os.path.exists(os.path.join(b,a)):
        c = open(os.path.join(b,a),'w')
    else:
        print("NO")
def Add_new_directory_to_this_directory():
    print("Name of directory?")
    a=str(input())
    print("What is the way of the directory")
    b=str(input())
    if os.path.exists(os.path.join(b)):
        os.mkdir(os.path.join(b,a))
    else:
        print("NO")

def Delete_file():
    print("Name of file?")
    a=str(input())
    print("What is the way of the directory?")
    b=str(input())
    if os.path.exists(os.path.join(b)):
        os.remove(os.path.join(b,a))
    else:
        print("NO")
def Rename_file():
    print("Old name of file?")
    a=str(input()) #old name of file
    print("New name of file?")
    b=str(input()) #new name of file
    print("Directory of file?")
    c=str(input()) #directory of file
    if os.path.exists(os.path.join(c,a)):
        old_file = os.path.join(c, a)
        new_file = os.path.join(c, b)
        os.rename(old_file, new_file)
    else:
        print("NO")
def Add_content_to_this_file():
    print("Name of file?")
    a=str(input())
    print("What is the way of the directory?")
    b=str(input())
    c=str(input("What you want to add?"))
    if os.path.exists(os.path.join(b,a)):
        f = open(os.path.join(b,a),'a')
        f.write(c + '\n')
    else:
        print("NO")
def Rewrite_content_of_this_file():
    print("Name of file?")
    a=str(input())
    print("What is the way of the directory?")
    b=str(input())
    c=str(input("What you want to add?"))
    if os.path.exists(os.path.join(b,a)):
        f = open(os.path.join(b,a),'w')
        f.write(c + '\n')
    else:
        print("NO")
def Return_to_the_parent_directory():
    print("Name of file?")
    a=str(input())
    print("What is the way of the directory?")
    b=str(input())
    if os.path.exists(os.path.join(b,a)):
        from pathlib import Path
        path = Path(b)
        print(path.parent)
    else:
        print("NO")



def Work_Directory():
    print('''
1 - Renama directory
2 - Print number of files
3 - Print number of directory
4 - List content of the directory
5 - Add file to this directory
6 - Add new directory to this directory''')
    b=int(input())
    if b==1:
        Renama_directory()
    if b==2:
        Print_number_of_files()
    if b==3:
        Print_number_of_directory()
    if b==4:
        List_content_of_the_directory()
    if b==5:
        Add_file_to_this_directory()   
    if b==6:
        Add_new_directory_to_this_directory()
            

def Work_File():
    print('''
1 - Delete file
2 - Rename file
3 - Add content to this file
4 - Rewrite content of this file
5 - Return to the parent directory''')
    b=int(input())
    if b==1:
        Delete_file()
    if b==2:
        Rename_file()
    if b==3:
        Add_content_to_this_file()
    if b==4:
        Rewrite_content_of_this_file()
    if b==5:
        Return_to_the_parent_directory()

def Start_game():
    print('''What do you waht?
1 - if work with directory.
2 - if work with file.''')
    a=int(input())
    if a==1:
        Work_Directory()
    if a==2:
        Work_File()

Start_game()