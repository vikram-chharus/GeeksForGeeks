#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:

    def subArraySum(self,arr, n, s): 
       tsum = arr[0]
       sp = 0
       index = 1
       while index <= n:
        if tsum == s:
            return [sp+1, index]
        if index > n and sp >= index or index == n and sp == n or tsum < s and index == n:
            break
        if tsum < s and index <n:
            tsum += arr[index]
            index += 1
        if tsum > s and sp <= index:
            tsum -= arr[sp]
            sp+= 1
       return [-1]

ob = Solution()
d = "174 98 1183 23"
a = [int(x) for x in d.split() ]
s = 1103
n = len(a)
print(ob.subArraySum(a, n, s))
