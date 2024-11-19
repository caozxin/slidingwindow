class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 1) find the identical string window
        # 2) always replace it to get the max length
        # 3) store the max length through iteration

        if k >= len(s):
            return len(s)

        # str_win = 
        max_rep = k
        ma_sub = k 

        #use left, right to define the window
        left, right = 0, 0
        while left <= right and right <= len(s):

            curr_char = s[left] # for each char, we need to find the longest possible substring
            
            while left <= right and right <= len(s) and k != 0:
                print(s[left], s[right+1])
                if s[left] != s[right+1]:
                    print(s[left], s[right+1])
                    exit()
                exit()
            # print(s[left:right])

            # #update win:
            # right += k
            # print(s[left:right+1])

            # if s[left] == s[right+1]:
            #     print('same')
            # print(s[left], s[right+1])

            

            exit()
