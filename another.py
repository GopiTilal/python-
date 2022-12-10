a = int(input("Enter a value of a:"))
b = int(input("Enter a value of b:"))
c = int(input("Enter a value of c:"))
exp = a**3+b**3+c**3+3+a*b+3+b*c+3+c*a
print("="*50)
print("exp({},{},{})={}".format(a, b, c,exp))
print("="*50)