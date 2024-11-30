from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """TODO:
            use left, right pointer to define window:
            keep track of current freq of each char and max_sub
            while k > 0:
                replace 1 char; update freq map and max_sub;
                move right += 1;
                k -= 1
            if max_sub < len(s):
                left += 1,right = left, k = k;
                continue k replacement looping
            if left = len(s) - k:
                return max_sub
        """
        # the best version: 
        string_length = len(s)
        length_of_max_substring = 0
        start = 0
        char_freq = {}
        most_freq_char = 0

        for end in range(string_length):
            if s[end] not in char_freq:
                char_freq[s[end]] = 1
            else:
                char_freq[s[end]] += 1

            most_freq_char = max(most_freq_char, char_freq[s[end]])

            if end - start + 1 - most_freq_char > k:
                char_freq[s[start]] -= 1
                start += 1
            
            length_of_max_substring = max(end - start + 1, length_of_max_substring)
            
        return length_of_max_substring
