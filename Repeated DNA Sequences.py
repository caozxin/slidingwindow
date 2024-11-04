#my version:
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
        
# improved version:
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        seen, repeated = set(), set()
        
        for i in range(len(s) - 9):
            window = s[i:i + 10]
            if window in seen:
                repeated.add(window)
            else:
                seen.add(window)
                
        return list(repeated)
