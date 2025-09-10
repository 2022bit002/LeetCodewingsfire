class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        ret=''

        i=0
        j=len(s)-1

        print(s)

        while s:
            ret+=s.pop()
            if len(s)>0:
                ret+=" "

        return ret

        