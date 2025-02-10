from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        count_t = Counter(t)
        required_chars = len(t)
        min_substr = ""
        min_len = float("inf")

        window_count = Counter()
        formed = 0  # Number of chars that match required frequency
        left = 0  # Left pointer for shrinking window

        for right in range(len(s)):  # Expanding window with for-loop
            char = s[right]
            window_count[char] += 1

            if window_count[char] <= count_t[char]:  
                formed += 1  # Increment only when contributing to required_chars

            # Contract the window while it contains all required characters
            while formed == required_chars:
                window_size = right - left + 1
                if window_size < min_len:
                    min_len = window_size
                    min_substr = s[left:right + 1]  # Update min substring

                # Remove leftmost character and move left pointer
                left_char = s[left]
                window_count[left_char] -= 1

                if window_count[left_char] < count_t[left_char]:  
                    formed -= 1  # If removal affects `t`'s required count, decrease `formed`

                left += 1  # Contract the window from the left

        return min_substr
