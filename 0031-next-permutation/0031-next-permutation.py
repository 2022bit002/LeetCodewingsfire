class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        pivot = 0


        for i in range(n-2,-1,-1):
            if nums[i+1]>nums[i]:
                pivot = i
                break
        else:
            nums.reverse()
            return nums

        for i in range(n-1,pivot,-1):
            if nums[i]>nums[pivot]:
                nums[i],nums[pivot]=nums[pivot],nums[i]
                break

        left = pivot+1
        right = n-1

        while left<right:
            nums[left],nums[right]= nums[right],nums[left]
            left+=1
            right-=1

        return nums

            







        