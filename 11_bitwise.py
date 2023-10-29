import operator as op
a=0;b=1
m=10
print("a and b are : ",a,b)
print()
print("Bitwise AND : ",op.and_(a,b))
print("Bitwise OR : ",op.or_(a,b))
print("Bitwise NOT : ",op.invert(b))
print("Bitwise XOR : ",op.xor(a,b))
print(m," is m before shifting Bitwise rightshift : ",m >> 1)
print(m," is m before shifting Bitwise Leftshift : ",m << 1)