def transitionPoint(arr, n):
    if n == 1:
        return -1

    cur_value = arr[0]
    isChanged = False
    for i in range(1,n):
        if cur_value != arr[i]:
            cur_value = i#saving the point
            isChanged = True
            break
    if isChanged:
        return cur_value
    else:
        return -1

d = [ int(x) for x in "1 3 5 2 2".split()]
n = len(d)    
print(transitionPoint(d, n))