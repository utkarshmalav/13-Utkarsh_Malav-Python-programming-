# Write a program for checking odd and even numbers from the tuple.

numb= (1, 2, 3, 4, 5, 6, 7, 8, 9,10,121,155,242)

for num in numb:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")
