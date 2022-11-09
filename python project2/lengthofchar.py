def count(names):
    total=0
    for i in names:
        if len(i)>5:
            total = total+1
        else:
            total = total
    return total
            
names = ["Atul","Shubham","Anurag","Rahul","dev","Roy"]
total=count(names)
print(total)