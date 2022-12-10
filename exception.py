try:
	print("try--Program Execution Strated:")
	s1=input("\nEnter First Value:")
	s2=input("Enter Second Value:")
	#convert str values into int
	a=int(s1) 
	b=int(s2) 
	c=a/b  
except ZeroDivisionError:
	print("\nDON'T ENTER ZERO FOR DEN...")
except ValueError:
	print("\nDON'T ENTER STRS,ALNUMS AND SYMBOLS")
else:
	print("------------------------------------")
	print("Val of a=",a)
	print("Val of b=",b)
	print("Div=",c)
	print("------------------------------------")
finally:
	print("\nfinally block--Program Execution Ended:")

