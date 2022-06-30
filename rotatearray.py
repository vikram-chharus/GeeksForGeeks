#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        show_values = []
        for i in range(N):
            if N-i >= D:
                temp = A[i]
                A[i] = A[i-D]
                A[i-D] = temp
                show_values = A
        return A


ob = Solution()
d = [ int(x) for x in "1 2 3 4 5".split()]
n = len(d)    
print(ob.rotateArr(d, 2, n))