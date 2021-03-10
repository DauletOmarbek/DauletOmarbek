class Student():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print(fname, lname)

fname=str(input())
lname=str(input())
x=Student(fname, lname)
x.printname()
