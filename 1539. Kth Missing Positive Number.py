class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        i,j=1,0
        for num in arr:
            while i<num:
                #print(i)
                j+=1
                i+=1
                if j==k: return i-1    
            i+=1  
        if j<k:return arr[-1]+(k-j)
        return i-2
