while(True):
	age=int(input("Enter Age of the Citizen:"))
	if(age>=18) and (age<=100):
		break
	print("Invalid, try again")
print("\n{} years citizen is eligible to vote".format(age))
