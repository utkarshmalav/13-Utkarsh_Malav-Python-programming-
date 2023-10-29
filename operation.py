l4=[]
n=int(input("Enter no. of elements : "))
for i in range(0,n):
    l4.append(input("Enter Element: "))
for i in l4:
    print("List Elements : ",i,end='')
print()
l4.remove('1')
print("l4.remove('1') : ",l4)

print("Length l4 : ",len(l4))
print("Min : ",min(l4))
print("Max : ",max(l4))