class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        p = max(dic.values())
       # print(p)
        sum = 0
        for i in dic:
            if dic[i]==p:
                sum+=p


        return sum 

