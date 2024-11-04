from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        if not s:
            return []

        left, right = 0, 9 
        res = []
        #  right  = k size

        k_list = []

        while right < len(s):
            window = s[left:right+1]
            # print(window, len(window))
            k_list.append(window)
            # print(k_list)
            left += 1
            right += 1
            # exit()

        # print(k_list)

        x = Counter(k_list)

        # print(x)
        
        for i in x.keys():
            # print(i, ":", x[i])
            if x[i] > 1:
                res.append(i)
        # print(res)

        return res
