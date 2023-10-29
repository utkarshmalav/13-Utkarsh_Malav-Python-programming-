amount=int(input("Enter the amount:  "))
if amount>1000:
    discount=amount*0.5
    print(discount)
elif amount<1000:
    discount=amount*0.2
    print(discount)
else:
    discount=amount*0.1
    print(discount)
