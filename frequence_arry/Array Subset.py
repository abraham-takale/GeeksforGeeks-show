#User function Template for python3
class Solution:
    def isSubset(self, a, b):
        freq={}
        for nums in a:
            freq[nums] = freq.get(nums,0) +1
        for num in b:
            if num not in freq or freq[num] ==0:
                return False
            freq[num]-=1
        return True
