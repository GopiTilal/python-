def empinfo(eno, ename, esalary, age,  dept="software", cnt="INDIA"):
    print("\t{}\t{}\t{}\t{}\t{}\t{}".format(eno, ename, esalary, age, dept, cnt))

# main program
print("-"*50)
print("\tNo\tName\tsalary\tAge\tDepartment\tcountry")
print("-"*50)
empinfo(101, "Tilak", 4000, 24)
empinfo(102, "Manohar", 4000, 24, "GOVT")
empinfo(101, "Vineeth", 4000, 24)
empinfo(101, "Manoj", 4000, 24)
empinfo(101, "Dhanush", 4000, 24)
empinfo(101, "prasad", age=24, esalary=45000)
print("-"*50)