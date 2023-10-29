l1 = [1, 2, "hello", 3.4]
print(l1, "\n")
print("Type:", type(l1))
print()

print("l1[2:]:", l1[2:])
print("l1[:]:", l1[:])
print("l1[1:4:2]:", l1[1:4:2])
print("l1[-3:-1]:", l1[-3:-1])

l1[2] = 10
print(l1)

l1[2:4] = [84, 36]
print(l1)

l2 = l1 * 2
print(l2)

print("Concatenation")
l3 = l1 + l2
print(l3)

print("Iteration")
for item in l1:
    print(item)

print("Membership")
print(1 in l1)
