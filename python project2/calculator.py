k=str(input("What you want to perform?"))
x=float(input("Enter the Number:"))
y=float(input("Enter the number:"))

def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)


if  k=='add':
    add(x,y)
elif k=='subtract':
    sub(x,y)
elif k=='multiply':
    multiply(x.y)
elif k=='divide':
    divide(x,y)