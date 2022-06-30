#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        dist_values = {}
        for i in range(n):
            if arr[i] in dist_values.keys():
                dist_values[arr[i]] += 1
            else:
                dist_values[arr[i]] =1

        pairs = 0
        for key in dist_values.keys():
            if k-key in dist_values.keys():
                pairs +=dist_values[key]

        return pairs
ob = Solution()
d = [ int(x) for x in "1 5 7 1".split()]
n = len(d)    
print(ob.getPairsCount(d, n, 6))