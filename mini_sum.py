#User function Template for python3

class Solution:
    def sumBetweenTwoKth(self, A, N, K1, K2):
        A.sort()
        sum = 0
        for i in range(K1, K2-1):
            sum+=A[i]
        return sum
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():
    a = [20, 8, 22, 4, 12, 10, 14]
    n =7 
    k1= 3
    k2 = 6
    ob=Solution()
    print( ob.sumBetweenTwoKth(a, n, k1, k2) )



if __name__ == "__main__":
    main()