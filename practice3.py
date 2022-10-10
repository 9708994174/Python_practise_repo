# A company decided to give bonus of 1000 to  
# employee if his/her service is more than 5 years 
# ask the user their salary and year of service and print the net bonus amount

currentSalary=int(input("Enter your current salary:"))
year=int(input("Enter your year of service: "))

if year>=5:
    print("Your salary is:",currentSalary+1000)
else:
    print("currentsalary")