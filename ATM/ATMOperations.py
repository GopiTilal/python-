from ATMExcept import DepositError,InsuffFundError,WithdrawError
bal=500.00 # Global Variable for Min Bal
def deposit():
	damt=float(input("Enter ur deposit amount:"))  #here PVM raise ValueError when damt is alnums,str,symbols
	if(damt<=0):
		raise DepositError
	else:
		global bal
		bal=bal+damt
		print("Ur Account xxxxxxx123 credited with INR:{}".format(damt))
		print("Now Ur Account  Bal:{}".format(bal))

def  withdraw():
	global bal
	wamt=float(input("Enter ur withdraw amount:"))  #here PVM raise ValueError when wamt is alnums,str,symbols
	if(wamt<=0):
		raise WithdrawError
	elif((wamt+500)>bal):
		raise InsuffFundError
	else:
		bal=bal-wamt
		print("Ur Account xxxxxxx123 debited with INR:{}".format(wamt))
		print("Now Ur Account  Bal:{}".format(bal))


def  balenq():
	print("Ur Account  Bal:{}".format(bal))