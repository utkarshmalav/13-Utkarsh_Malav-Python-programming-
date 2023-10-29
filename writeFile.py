file=open("input.txt","w")
w="hello\n"
file.writelines(["I am Shruti Ugale\n","My Roll No is 4\n","I am student of DYPCET\n"])
print(file.write(w))

file=open("input.txt","r")
print(file.read())
