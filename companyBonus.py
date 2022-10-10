salary=int(input("Enter the salary"))
year=int(input("Enter the year"))

if year>10:
    print((10/100)*salary,"your salary")
elif year>6 and year<10:
    print((8/100)*salary,"your salary")

elif year<6:
    print((5/100)*salary,"your salary")
