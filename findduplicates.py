from tkinter import SOLID


class Solution:
    def duplicates(self, arr, n): 
        data = {}
        result = list()
        for i in range(n):
            if arr[i] in data.keys():
                data[arr[i]] += 1
            else:
                data[arr[i]] = 1
        for key in data.keys():
            if data[key] > 1:
                result.append(key)    
        if result:
            result.sort()
            return result
        else:
            return [-1]

d = [int(x) for x in "0 3 1 2".split()]
n = len(d)
s = Solution().duplicates(d, n)
for i in s:
    print(i, end=' ')