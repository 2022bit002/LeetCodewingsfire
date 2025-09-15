class Solution:
    def canBeTypedWords(self, text: str, b: str) -> int:
        c=0
        b = set(b)
        w = text.split(' ')

        for i in w:
            for t in i:
                if t in b:
                    c+=1
                    break



        return len(w)-c



            
            




