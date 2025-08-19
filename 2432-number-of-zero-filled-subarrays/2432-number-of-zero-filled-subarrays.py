class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        fact = 1
        count = 0
        i=0
        zero = 0

        while i<len(nums):
            if nums[i]==0:
                zero+=1
                fact *= zero
                count+=zero
            else:
                zero = 0
                fact =1
            i+=1

        return count
            