#Remove Vovels

str1 = input("\nEnter the string: ")
l1 = list(str1)
vo = ['a', 'e', 'i', 'o', 'u']
new_list = []

for char in l1:
    if char not in vo:
        new_list.append(char)

result = "".join(new_list)
print("After removing vovels : ",result)
