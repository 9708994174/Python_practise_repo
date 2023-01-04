#function is same but doing work for all datatypes like string , list ,integer
a="Hello"
b=[1,2,3,4]
print("Lenth of list is : ",len(b))   

def add(a,b,c=0):
    return a+b+c
print(add(1,2))
print(add(1,2,3))  # overloading
