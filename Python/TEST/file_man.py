import os, os.path, time

def Rename_directory():
    print("What is the way of the directory")
    b= str(input())
    if os.path.exists(b):
        print('What the new name')
        c = str(input())
        os.rename(b, c)

def Number_files():
    print("What is the way of the directory")
    b =str(input())
    if os.path.exists(b):
        c = len([name for name in os.listdir(b) if os.path.isfile(os.path.join(b, name))])
        print(c)

def Change_directory():
    b= str(input('''What the directory'''))
    os.chdir(b)
    print("Directory changed")
    s = input()
    if s== 'd' or s == 'D':
        Work_directory()
    elif s == "f" or s=='F':
        Change_directory()  



def Work_directory():
    print('''
    1 - remane directory
    2 - number of files in directory
    3 - change directory
    ''')
    command = input()
    if command == '1':
        Rename_directory()
    if command == '2':
        Number_files()
    


def Start_game():
    print('''What do you what?
    -If work with directory press d or D
    -If work with file press f or F
    ''')
    s = input()
    if s== 'd' or s == 'D':
        Work_directory()
    elif s == "f" or s=='F':
        Change_directory()  


Start_game()