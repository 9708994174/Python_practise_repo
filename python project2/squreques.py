#x = lambda a:a*a
#num = x(5)
#print(num)


def name(x,y):
    return lambda a: a + x 

num = name(10)
print(num(10,20))

