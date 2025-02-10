from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return
        # print("hello")
        if not s or not t:
            return ""
        # --> below are required
        # t = 'a'
        # s = 'abs'
        count_t = Counter(t) 
        len_t = len(t)
        min_sub_b = ""

        print(count_t, len_t)

        left, right = 0, 0
        for left in range(len(s)):
            
            sub_s = s[left:right + 1]
            curr_len = right - left + 1

            if right < len(s) and curr_len < len_t: #1) condition
                right += 1
            elif set(sub_s).issubset(set(t)): # 2) condition, atm curr_len >= len_t:
                print(sub_s)
                print("matching t")
                if len(min_sub_b) == 0 or len(sub_s) <= len(min_sub_b):
                    min_sub_b = sub_s
                    print("new min: ", min_sub_b)
                left += 1
            # exit()

        return min_sub_b
