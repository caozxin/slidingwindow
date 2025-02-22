class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if not nums: # none handling
            return 0
        
        # set variables
        n = len(nums)
        min_len = float('inf')
        curr_sum = 0
        left, right = 0, 0

        for right in range(n):
            curr_len = right - left + 1
            curr_sum += nums[right]
            window = nums[left:right+1]
            print(curr_sum, window)

            if curr_sum < target:
                min_len = min(min_len, right - left + 1)
                right += 1
                
            else:
                left += 1
                curr_sum -= nums[left]
                # print("curr_len", curr_len, window)
                # print("min_len", min_len)
            
        return min_len if min_len < n else 0
