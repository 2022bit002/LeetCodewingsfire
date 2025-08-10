class Solution:
    def countElements(self, nums: List[int]) -> int:
        ar = []
        if len(nums)<2:
            return 0
        nums.sort()
        if nums[0]==nums[-1]:
            return 0
        return len(nums) - nums.count(nums[0]) - nums.count(nums[-1])
        