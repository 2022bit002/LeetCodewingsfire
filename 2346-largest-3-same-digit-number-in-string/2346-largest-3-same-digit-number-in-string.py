class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good_int=['999','888','777','666','555','444','333','222','111','000']
        for i in good_int:
            if i in num:
                return i
        return ''