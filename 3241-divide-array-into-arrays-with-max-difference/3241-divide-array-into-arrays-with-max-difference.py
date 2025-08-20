class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:


        nums.sort()
        #print(nums)
        i = 1
        j = 0
        ret = [[nums[0]]]
        while i<len(nums):
            if len(ret[-1])<3:
                ret[-1].append(nums[i])
           

            i+=1
            j=i-1

            if len(ret[-1])==3 and i<len(nums):
                ret.append([])

        for i in range(len(ret)):
            if ret[i][-1] - ret[i][0]>k:
                return []


        return ret




        