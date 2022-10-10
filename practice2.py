#take values of length and breadth from the user 
#print if it is a square or not

length = int(input("Enter the value of length"))
breadth = int(input("Enter the value of breadth"))
if length == breadth:
    print("it is a square")
else:
    print("it is a rectangle")