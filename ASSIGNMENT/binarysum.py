#Addition of 2 Binary Numbers... 

def binarySum(x, y):
    if len(x) > len(y):
        return binarySum(y, x)

    diff = len(y) - len(x)
    padding = '0' * diff
    x = padding + x
    res = []
    carry = '0'

    for i in range(len(x) - 1, -1, -1):
        if x[i] == '1' and y[i] == '1':
            if carry == '1':
                res.append('1')
                carry = '1'
            else:
                res.append('0')
                carry = '1'
        elif x[i] == '0' and y[i] == '0':
            if carry == '1':
                res.append('1')
                carry = '0'
            else:
                res.append('0')
                carry = '0'
        else:
            if carry == '1':
                res.append('0')
                carry = '1'
            else:
                res.append('1')
                carry = '0'

    if carry == '1':
        res.append(carry)

    return ''.join(res[::-1]).lstrip('0')

a = "101"
b = "1001"
print("Sum of ",a," & ",b," is ",binarySum(a, b))