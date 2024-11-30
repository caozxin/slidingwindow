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
        # # the best version: 
        # string_length = len(s)
        # length_of_max_substring = 0
        # start = 0
        # char_freq = {}
        # most_freq_char = 0

        # for end in range(string_length):
        #     # update the freq of end char:
        #     if s[end] not in char_freq:
        #         char_freq[s[end]] = 1 
        #     else:
        #         char_freq[s[end]] += 1

        #     most_freq_char = max(most_freq_char, char_freq[s[end]]) 
        #     #max substring without repeating char is actually the max freq of a char after replacement

        #     if end - start + 1 - most_freq_char > k: # if the current substring needs replacement greater than k, we move start 1 step
        #         char_freq[s[start]] -= 1
        #         start += 1
            
        #     length_of_max_substring = max(end - start + 1, length_of_max_substring) # update length_of_max_substring at each step
            
        # return length_of_max_substring

        # my version:

        #none handeling:
        if len(s) < k or len(s) == 0:
            return k or 0

        left, right = 0, 0
        length_of_max_substring = 0
        char_freq = {}
        most_freq_char = 0



        while right < len(s):
            #always update freq of right char:
            if s[right] not in char_freq:
                char_freq[s[right]] = 1
            else:
                char_freq[s[right]] += 1
            # print(char_freq)
            # exit()
            most_freq_char = max(most_freq_char, char_freq[s[right]])
            # print(most_freq_char)
            # exit()
            # Check if the current window is valid
            if (right - left + 1) - most_freq_char > k:
                # Shrink the window
                char_freq[s[left]] -= 1
                left += 1

            # Update the maximum length of valid substring
            length_of_max_substring = max(length_of_max_substring, right - left + 1)

            # Expand the window
            right += 1

        return length_of_max_substring
