#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        
        index = arr.index(max(arr))
        if len(arr) != index+1:
            return index+1
        else:
            return 0


ob = Solution()
d = [ int(x) for x in "5 4 3 ".split()]
n = len(d)    
print(ob.findKRotation(d, n))