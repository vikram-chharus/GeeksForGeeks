#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:

    def subArraySum(self,arr, n, s): 
       tsum = 0
       for i in range(n):
        tsum = arr[i]
        index = i+1
        while index <= n:
            if tsum == s:
                return [i+1, index]
            if tsum > s or index >= n:
                break
            if tsum < s:    
                tsum += arr[index]
                index +=1   
       return [-1]
ob = Solution()
d = "142 112 54 69 148 45 63 158 38 60 124 142 130 179 117 36 191 43 89 107 41 143 65 49 47 6 91 130 171 151 7 102 194 149 30 24 85 155 157 41 167 177 132 109 145 40 27 124 138 139 119 83 130 142 34 116 40 59 105 131 178 107 74 187 22 146 125 73 71 30 178 174 98 113"
a = [int(x) for x in d.split() ]
s = 665
n = 74
print(ob.subArraySum(a, n, s))