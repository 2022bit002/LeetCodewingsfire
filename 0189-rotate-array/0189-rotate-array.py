class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        if k==0:
            return nums
        
        l=0
        r=len(nums)-1
        m=(k-1)%len(nums)
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        l=0
        r=len(nums)-1
        m=(k-1)%len(nums)
        while l<m:
            nums[l],nums[m] = nums[m],nums[l]
            l+=1
            m-=1
        l=0
        r=len(nums)-1
        m=k%len(nums)

        while m<r:
            nums[m], nums[r]=nums[r],nums[m]
            m+=1
            r-=1







