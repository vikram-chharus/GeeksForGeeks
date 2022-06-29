#User function Template for python3

from operator import indexOf


class Solution:
    def canReach(self, A, N):
        # code here 
        max_jumps = A[0]
        cur_position = 0
        while True:
            if cur_position >= N:
                return 1
            new_max = max(A[cur_position:max_jumps])
            cur_position = new_max


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    A=[ int(x) for x in "5 9 3 2 1 0 2 3 3 1 0 0".split()]
    N=len(A)   
    ob = Solution()
    print(ob.canReach(A,N))
# } Driver Code Ends