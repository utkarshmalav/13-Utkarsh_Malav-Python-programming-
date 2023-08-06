# Write a Python program for extracting the vowels from the string and display its count.

S = "Its Uttu here, I am cse student at DYPCET"
vowels = "AEIOUaeiou"
count = 0
for char in S:
    if char in vowels:
        count += 1
print("Number of vowels in string S : ", count)
