class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        p = n

        count = 0

        while p>1:
            #print(p)
            count+=1
            p/=4
        #print((count))
        return n == 4**count