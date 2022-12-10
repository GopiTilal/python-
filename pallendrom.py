lst = ["MOM", "DAD", "LIRIL", "MADAM", "PYTHON", "CAR"]
hp1 = 0
ind = -1
for i in range(0, len(lst)):
    c1 = 0
    cv = str(lst[i])
    if(cv == cv[::-1]):
        c1 = len(cv)
    if(c1 > hp1):
        hp1 = c1
        ind = ind
print("Highest palindrome={}".format(lst[ind]))
print("{} whose length is {}".format(lst[ind], hp1))
