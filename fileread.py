#file handling

#using for loop
file=open('input.txt','r')
for a in file:
    print(a)

#read
file=open("input.txt",'r')
print(file.read(5))

#with statement
with open("input.txt",)as file:
    data=file.read(18)
print(data)

#to read certain number of char
file=open("input.txt",'r')
print(file.read(5))

#readline
file=open("input.txt",'r')
print(file.readline(8))
file.seek(0)
print(file.readlines())
file.close()
