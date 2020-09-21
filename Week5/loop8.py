for i in range(10):
    for j in range(10):
        if j < i:
            print(" ", end=" ")
        else:
            print(j-i, end=" ")
    print()
