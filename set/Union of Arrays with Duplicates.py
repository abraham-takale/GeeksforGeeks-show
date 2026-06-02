class Solution:    
    def findUnion(self, a, b):
        # code here
        se1=set(a)
        se2=set(b)
        return se1 | se2
