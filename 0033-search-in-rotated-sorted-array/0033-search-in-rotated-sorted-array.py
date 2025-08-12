from typing import List

class Solution:
    def search(self, arr: List[int], target: int) -> int:
        l = 0
        r = len(arr) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if arr[mid] == target:
                return mid
            
            # Left half is sorted
            if arr[l] <= arr[mid]:
                if arr[l] <= target < arr[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            # Right half is sorted
            else:
                if arr[mid] < target <= arr[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1
