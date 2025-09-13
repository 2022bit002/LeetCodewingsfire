class Solution:
    def smallestRangeII(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr.sort()
        
        res = arr[-1] - arr[0]
        
        for i in range(1,len(arr)):
            
            minH = min(arr[0]+k, arr[i]-k)
            maxH = max(arr[-1]-k, arr[i-1]+k)
            res = min(res, maxH-minH)
            
        return res
        