class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        count=0
        if n==1:
            return True
        if n>1 and n%3==0:
            q=n
            
            while q>1:
                q//=3
                count+=1


        
        return 3**count == n