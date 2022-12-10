def sumop():
    a = int(input("Enter value of a:"))
    b = int(input("Enter value of b:"))
    c = a+b
    return a,b,c
# main program
a,b,c = sumop()
print("sum({},{})={}".format(a,b,c))
print("="*50)
hyd = sumop()
print("sum({},{})={}".format(hyd[-3],hyd[-2],hyd[-1]))
