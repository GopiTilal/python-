#SimpleIntFunEx2.py
def  simpleint():
	p=float(input("Enter Principle Amount:"))
	t=float(input("Enter  Time:"))
	r=float(input("Enter Rate of Interest:"))
	if(p<0) or (t<0) or (r<0):
		return tuple()     #  OR  return  ()   here  () is called empty tuple
	else:
		#cal  si and totamt
		si=(p*t*r)/100
		totamt=p+si
		return p,t,r,si,totamt

#main program
res=simpleint()
print("Number of values in res=",len(res))
if(len(res)>0):
	print("="*40)
	print("Simple Interest Calculations")
	print("="*40)
	print("Principle Amount:{}".format(res[0]))
	print("Time:{}".format(res[1]))
	print("Rate of Interest:{}".format(res[2]))
	print("Simple  Interest:{}".format(res[3]))
	print("Total Amount to Pay:{}".format(res[4]))
	print("="*40)
else:
	print("Invalid Inputs:")