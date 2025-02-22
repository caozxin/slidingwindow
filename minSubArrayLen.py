from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        min_len = float('inf')
        curr_sum = 0
        left = 0

        for right in range(n):
            curr_sum += nums[right]
            
            while curr_sum >= target:  # Try to shrink the window
                min_len = min(min_len, right - left + 1)
                curr_sum -= nums[left]
                left += 1  # Move the left boundary
                
        return min_len if min_len != float('inf') else 0
