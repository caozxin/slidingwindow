from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # return

        def check_counters(counter_a: list, counter_b: list):

            for each in counter_a:
                if counter_a[each] <= counter_b[each]:
                    # print("matching")
                    pass
                else:
                    return False
            return True


        if  not s or not t: # none handling
            return ""
        # s = 'a'
        # t = 'aa'
        count_t = Counter(t)

        print(count_t)

        count_s = Counter(s)

        if not check_counters(count_t,count_s): # if the whole string does not contain t at all
            return ""

        print(check_counters(count_t,count_s))

        # left, right = 0, 0
        min_sub = len(s)
        min_sub_s = ''


        for left in range(len(s)):
            right = left
            sub_s = s[left:right+1]
            print(sub_s)
            while check_counters(Counter(sub_s), count_t) and right < len(s):
                print("true sub", sub_s, left, right)
                if min_sub > len(sub_s):
                    print("sub_s", sub_s)
                    min_sub_s = sub_s
                    min_sub = len(min_sub_s)
                right +=1
                sub_s = s[left:right+1] 
            print("not true sub")
            exit()
        


