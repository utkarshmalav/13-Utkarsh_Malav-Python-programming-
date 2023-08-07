# Write a program for sorting the numbers declared in the list using insertion sort. 

numb = [12,2.2,2.001,11,3,5,6,0]
print("Unsorted list : "numb)
for i in range(1, len(numb)):
    key = numb[i]
    j = i - 1
    while j >= 0 and key < numb[j]:
      numb[j + 1] = numb[j]
      j -= 1
    numb[j + 1] = key
print("Sorted list : "numb)
