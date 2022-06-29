class Solution:
    def MissingNumber(self,array,n):
        array.sort()
        for i in range(n-1):
            if i != array[i]-1:
                return i+1 
        return n
ob = Solution()
d = [ int(x) for x in "1".split()]
n = len(d)+1

print(ob.MissingNumber(d, n))
