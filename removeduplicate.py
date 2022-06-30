def remove_duplicate(A, N):
    index = 0
    while index+1 < len(A):
        if A[index] == A[index+1]:
            A.pop(index+1)
        else:
            index+=1

A = [1, 2, 2, 2, 3]
N = len(A)
remove_duplicate(A, N)
print(A)