str="Hello"
print(str[0])
print(str[-1])
print()

#String Reverse

print("String : ",str)
print("Reversed String :",str[::-1])
print()

#String Slicing

print("String : ",str)
print("Slicing : ",str[2:4])
print()

#String Character Updation

print("String : ",str)
list1=list(str)
list1[0]='c'
str1=''.join(list1)
print("Updated String: ",str1)
print()

#Delete String

print("String : ",str)
str1=str[0:2]+str[3:]
print("Sfter deletion: ",str1)
print()

#Delete Entire string

print("String : ",str)
str1=str
del str1
#print(str1)
print()


