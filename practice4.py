totalClass=int(input("Enter the number of total class:"))

attendClass=int(input("Enter the number of class you attended:"))

percentage =((attendClass)/(totalClass))*100

if percentage>=75:
    print("Your are elligable for exam")
else:
    print("Your are not elligable for exam")