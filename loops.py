
print("For Loop")
l=["first",1,2.0]
for i in l:
    print(i)


print("\nCountinue Statement")
for l in 'dypcetkop':
    if l=='e' or l=='p':
        continue
    print(l)

print("\nBreak Statement")
for l in 'dypcetkop':
    if l=='e' or l=='p':
        break
    print(l)

print("\nPass Statemnt")
for l in 'dyp123':
    pass
print("Last letter ",l)


print("\nWhile loop")
count=0
while count<3:
    count=count+1
    print("hello")
print("\n")
a=[1,2,3,4,5]
print("a=[1,2,3,4,5]")
while a:
    print(a.pop())

print("\nelse in while")

count=0
while count<5:
    print(count)
    count=count+1
else:
    print(count)
    
