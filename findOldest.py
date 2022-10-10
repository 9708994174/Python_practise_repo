#take input of age from 3 person
#determine the oldest and youngest

age1=int(input("Enter the first age:"))
age2=int(input("Enter the second age:"))
age3=int(input("Enter the third age:"))

if age1>age2 and age1>age3:
    print("Oldest is",age1)

elif age2>age1 and age2>age3:
    print("Oldest is",age2)
elif age3>age1 and age3>age2:
    print ("Oldest is ",age3)

if age1<age2 and age1<age3:
    print("Greatest is",age1)

elif age2<age1 and age2<age3:
    print("Greatest is",age2)
elif age3<age1 and age3<age2:
    print ("Greatest is ",age3)
