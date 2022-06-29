class Solution:
    def MissingNumber(self,array,n):
        numbers = 0
        sum= 0
        for i in range(n-1):
            numbers +=i+1
            sum += array[i]
        numbers +=n
        return int(numbers-sum)
ob = Solution()
d = [ int(x) for x in "1 2 3 4 6 7".split()]
n = len(d)+1

print(ob.MissingNumber(d, n))
