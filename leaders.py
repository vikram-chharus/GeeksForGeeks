
class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        leaders = []
        max_ = A[N-1]
        for i in range(N-1, 0, -1):
            if A[i] >= max_:
                max_ = A[i]
                leaders.append(A[i])
               
        leaders.reverse() 
        return leaders
ob = Solution()
d = [ int(x) for x in range(2723)]
n = len(d)    
print(ob.leaders(d, n))