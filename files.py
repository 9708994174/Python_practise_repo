#f=open("demo.txt","r")
# #print(f.read())
# # print(f.readline())
# # print(f.readline())


# f1=open("demo1.txt","w")
# f1.write("This is a new file")


# f2=open("myfile.txt","w")
# f2.write("My name is rahul \n")
# f2.write("I am a computer Science Student\n")

# # for i in f:
#     f2.write(i)


# try:    
#     f=open("demo.txt")
#     # your code goes here
# finally:
#     f.close()
# This way we are making sure that file is closed
#  properly even if exception is raised that cause the
#  programme flow to stop

# with open("demo.txt") as f:
#     f.read()
#     # your code goes here

# f=open("demo1.txt","r")
# print(f.read(1))
# print(f.tell())

# f=open("punjab.png","rb")
# f1=open("punjab_copy.png","wb")
# #print(f.read())

# for i in f:
#     f1.write(i)

import os
if os.path.exists("demo.txt"):

    os.remove("demo.txt")
else:
    print("File does not exits")


