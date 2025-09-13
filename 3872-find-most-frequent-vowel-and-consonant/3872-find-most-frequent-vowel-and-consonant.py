class Solution:
    def maxFreqSum(self, s: str) -> int:
        dic= {}
        v ="aeiou"
        vc = 0
        cc = 0

        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1

        for i in dic:
            #print(i)
            if i in v:
                if dic[i]>vc:
                    vc = dic[i]
            else:
                if dic[i]>cc:
                    cc = dic[i]


        return vc+cc


        
        