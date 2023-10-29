def remove_duplicate(s):
    c = list(s)
    index = 0
    length = len(s)

    for i in range(length):
        j = 0
        while j < i:
            if c[i] == c[j]:
                break
            j += 1

        if i == j:
            c[index] = c[i]
            index += 1

    s = ''.join(c[:index])
    return s

def remove_white_space(ch, key):
    c = list(key)

    for i in range(len(c)):
        for j in range(len(ch)):
            if c[i] == ch[j]:
                c[i] = ' '

    key = ''.join(c)
    key = key.replace(" ", "")

    return key

def make_pair(pt):
    s = ""
    c = 'a'

    for i in range(len(pt)):
        if pt[i] == ' ':
            continue
        else:
            c = pt[i]
            s += pt[i]

        if i < len(pt) - 1:
            if pt[i] == pt[i + 1]:
                s += "x"

    if len(s) % 2 != 0:
        s += "x"

    return s

def find_ij(a, b, x):
    y = [0] * 4

    if a == 'j':
        a = 'i'
    elif b == 'j':
        b = 'i'

    for i in range(5):
        for j in range(5):
            if x[i][j] == a:
                y[0] = i
                y[1] = j
            if x[i][j] == b:
                y[2] = i
                y[3] = j

    return y

def encrypt(pt, x):
    ch = list(pt)

    for i in range(0, len(pt), 2):
        if i < len(pt) - 1:
            a = find_ij(pt[i], pt[i + 1], x)

            if a[0] == a[2]:
                ch[i] = x[a[0]][(a[1] + 1) % 5]
                ch[i + 1] = x[a[2]][(a[3] + 1) % 5]
            elif a[1] == a[3]:
                ch[i] = x[(a[0] + 1) % 5][a[1]]
                ch[i + 1] = x[(a[2] + 1) % 5][a[3]]
            else:
                ch[i] = x[a[0]][a[3]]
                ch[i + 1] = x[a[2]][a[1]]

    pt = ''.join(ch)
    return pt

def main():
    pt = "instruments"
    key = "monarchy"

    key = remove_duplicate(key)
    ch = list("abcdefghiklmnopqrstuvwxyz")
    st = remove_white_space(ch, key)
    c = list(st)

    x = [['' for _ in range(5)] for _ in range(5)]
    index_of_st = 0
    index_of_key = 0

    for i in range(5):
        for j in range(5):
            if index_of_key < len(key):
                x[i][j] = key[index_of_key]
                index_of_key += 1
            else:
                x[i][j] = c[index_of_st]
                index_of_st += 1

    for i in range(5):
        for j in range(5):
            print(x[i][j], end=" ")
        print()

    pt = make_pair(pt)
    pt = encrypt(pt, x)

    print(pt)

if __name__ == "__main__":
    main()
