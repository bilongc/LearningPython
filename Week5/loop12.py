for i in range(1, 10):
    for j in range(1, 10):
        if (j < 10 - i):
            print(" ", end = " ")
        else:
            print(j - (9 - i), end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

for i in range(1, 10):
    for j in range(1, 10):
        if j <= i:
            print(" ", end=" ")
        else:
            print(j-i, end=" ")
    for j in range(8-i, 0, -1):
        print(j, end=" ")
    print()
