class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in nums[i+1:]:
                return [i,dic[target -nums[i]]]

        return False