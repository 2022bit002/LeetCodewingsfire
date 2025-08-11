class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        index=0
        count =1

        for i in range(1, len(nums)):
            if nums[i]==nums[index]:
                count+=1
            else:
                count-=1

            if count==0:
                index=i
                count=1

        return nums[index]