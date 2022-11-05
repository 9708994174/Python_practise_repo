a=int(input())
if 1<=a<=360:
    if a<90:
        print("Acute angle")
    elif a==90:
        print("Right angle")
    elif 180>a>90:
        print("Obtuse angle")
    else:
        print("invalid")