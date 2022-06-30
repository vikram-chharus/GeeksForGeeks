# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        left = 0
        right = N-1
        left_sum = A[left]
        right_sum = A[right]
        while left < right:
            if left_sum < right_sum:
                left += 1
                left_sum += A[left]
            elif left_sum > right_sum:
                right -= 1
                right_sum += A[right]
            elif left_sum == right_sum and left+1 != right-1:
                left += 1
                left_sum += A[left]
            elif left_sum == right_sum and left+1 == right-1:
                return left+2
 

ob = Solution()
d = [ int(x) for x in "1 3 5 2 2".split()]
n = len(d)    
print(ob.equilibriumPoint(d, n))
