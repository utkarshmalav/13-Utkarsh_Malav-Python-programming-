#Even Or Odd using tuples

length = int(input("Enter the number of total numbers: "))
t = []
print("Enter Numbers : ",end="")
for i in range(length):
    num = int(input())
    t.append(num)

even = []
odd = []

print("Tuple elements are ", t)

for i in range(length):
    if t[i] % 2 == 0:
        even.append(t[i])
    else:
        odd.append(t[i])

print("Even values are ", even)
print("Odd values are ", odd)
