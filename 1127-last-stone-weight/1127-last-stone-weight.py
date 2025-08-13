class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones)>1:
            n1 = max(stones)
            stones.remove(n1)
            n2 = max(stones)
            stones.remove(n2)
            if n1!=n2 :
                stones.append(n1-n2)

        if len(stones)==0:
            return 0
        return stones[-1]
         
