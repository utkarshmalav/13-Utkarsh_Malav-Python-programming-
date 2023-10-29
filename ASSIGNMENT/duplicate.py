l = list()
dupli = list()
size = int(input("Enter No Total Numbers : "))
print("Enter ", size, "Numbers : ",end="")
for i in range(0, size):
    n = int(input())
    l.append(n)

l_copy = l[:]

for i in range(0, size):
    num = l[i]
    for j in range(i + 1, size):
        if l[j] == num:
            if num not in dupli:
                dupli.append(num)
l = list(set(l))

print("List without duplicates:", l)
print("Duplicate elements:", dupli)
