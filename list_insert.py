numbers = [1,2,3,4,5,2,6]
for i in numbers:
    if i==2:
         g=numbers.index(i)
         numbers.remove(i)
         numbers.insert(g,200)
         break
print(numbers)