class Solution:
    def isSorted(self, arr) -> bool:
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                return False
        return True
                
        # code here
        
