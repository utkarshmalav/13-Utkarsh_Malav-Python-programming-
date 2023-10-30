file=open("input.txt","w")
w="hello\n"
file.writelines(["I am Utkarsh Malav\n","My Roll No is 13\n","I am student of DYPCET\n"])
print(file.write(w))

file=open("input.txt","r")
print(file.read())
