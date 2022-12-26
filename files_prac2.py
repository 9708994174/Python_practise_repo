try:    
    f=open("demo.txt")
    # your code goes here
finally:
    f.close()
# This way we are making sure that file is closed
#  properly even if exception is raised that cause the
#  programme flow to stop

with open("demo.txt") as f:
    f.read()
    # your code goes here

f=open("demo1.txt","r")
print(f.read(1))
print(f.tell())