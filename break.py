s = "PYTHON"
print("\n---for lopp without break statement--")
for ch in s:
 print("\t{}".format(ch))
else:
 print("I am from else-part-of-for loop")
print("\n----for loop with break statement---")
#display PYT
for v in s:
 if(v=="H"):
 break
else:
 print("\t{}".format("v"))
else:
print("i am from else-part-of-for loop")
print("\n other statement in program")