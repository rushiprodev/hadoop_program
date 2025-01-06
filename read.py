# f=open("demofile.txt", "r")
# #read a file 
# print(f.read())

# f=open("demofile.txt",'r')
# print(f.read(5))

#write a file 

# f=open("hello.txt", 'x')
f=open("hello.txt",'a')

f.write("now the file has more content")
f.close()