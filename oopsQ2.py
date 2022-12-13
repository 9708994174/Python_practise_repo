class person:
    def __init__(self,name,roll) -> None:
        self.name = name
        self.roll = roll



    def printOut(self):
        print("My name is :",self.name,"and my roll number is : ",self.roll)

person1 = person("Rahul","A24")
person2 = person("Aman","A23")

person1.printOut()
person2.printOut()

print(id(person1))
print(id(person2))