def convertWave( a, n):

    if n/2 == 0:
        for i in range(0, int(n), 2):
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
    else:
        for i in range(0, int(n-1), 2):
            temp = a[i]
            a[i] = a[i+1]
            a[i+1] = temp
a = [1, 2, 3, 4, 5]
convertWave(a, 5)
# print(a)
a.pop(0)
print(a)