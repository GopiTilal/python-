#student info by using class and object.
#program starts
class student:
    crs="python"

#main program
s1=student()
s2=student()
print("="*50)
print("Enter first student info")
print("="*50)
s1.stno=int(input("Enter student number:"))
s1.sname=int(input("Enter student name:"))
s1.marks=float(input("Enter student marks"))
print("="*50)
print("Enter second student info")
print("="*50)
s2.stno=int(input("Enter student number"))
s2.sname=int(input("Enter student name"))
s2.marks=float(input("Enter student marks"))
print("="*50)
print("Display first student info")
print("student number={}".format(s1.stno))
print("student name={}".format(s1.sname))
print("student marks={}".format(s1.marks))
print("student crs={}".format(student.crs))
print("="*50)
print("Display second student info")
print("="*50)
print("student number={}".format(s2.stno))
print("student name={}".format(s2.sname))
print("student marks={}".format(s2.marks))
print("student crs={}".format(student.crs))
print("="*50)
