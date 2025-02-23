class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # if not nums:
        #     return 0.0

        # max_sum = float('-inf')
        curr_sum = sum(nums[0:k])
        max_sum = curr_sum
        # print(curr_sum)

        for right in range(k, len(nums)):
            
            left = right - k 
            # print(left, right, nums[left:right])
            curr_sum -= nums[left]
            curr_sum += nums[right]
            max_sum = max(max_sum, curr_sum)

        
        return max_sum/k if max_sum != float('-inf') else 0.0
