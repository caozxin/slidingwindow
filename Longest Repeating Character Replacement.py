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

        if k >= len(s):
            return len(s)

        # str_win = 
        max_rep = k
        max_sub = 0 

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
