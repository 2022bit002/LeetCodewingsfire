class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dic1, dic2 ={}, {}

        for i in s:
            dic1[i] =1+ dic1.get(i, 1)

        for j in t:
            dic2[j] =1+ dic2.get(j , 1)

        print


        return dic1==dic2