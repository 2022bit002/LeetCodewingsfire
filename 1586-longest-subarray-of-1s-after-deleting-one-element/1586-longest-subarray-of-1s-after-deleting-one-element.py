class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i=0
        j=0
        l=0
        arr=[]
        

        for i in range(len(nums)):
            if nums[i]==0:
                if 0 in arr:
                    while 0 in arr:
                        arr.pop(0)
            arr.append(nums[i])
            l = max(l,len(arr)-1)


        return l