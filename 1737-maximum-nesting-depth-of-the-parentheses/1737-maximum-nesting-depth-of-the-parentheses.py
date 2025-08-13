class Solution:
    def maxDepth(self, s: str) -> int:
        stk = 0
        count =0

        for i in s:
            if i == '(':
                count+=1
            elif i ==')':
                count -= 1
            stk = max(stk,count)

        return stk


            