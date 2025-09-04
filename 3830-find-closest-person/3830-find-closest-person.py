class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        Person1=abs(x-z)
        Person2=abs(y-z)

        if Person1<Person2:
            return 1
        elif Person1>Person2:
            return 2

        return 0
        