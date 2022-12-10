def empinfo(eno, ename, esalary, age,  dept="software", cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}\t{}".format(eno, ename, esalary, age, dept, cnt))

# main program
print("-"*50)
print("\tNo\tName\tsalary\tAge\tDepartment\tcountry")
print("-"*50)
empinfo(101, "Tilak", 4700, 24)
empinfo(102, "Manohar", 4600, 23, "GOVT")
empinfo(103, "Vineeth", 4300, 25)
empinfo(104, "Manoj", 4400, 25)
empinfo(105, "Dhanush", 4500, 24)
empinfo(106, "prasad", 4700, 24)
print("-"*50)
