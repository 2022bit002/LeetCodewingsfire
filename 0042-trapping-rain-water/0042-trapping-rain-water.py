class Solution:
    def trap(self, height: List[int]) -> int:
        # array preprocessing
        maxNo = 0
        lArr=[]
        for i in height:
            if i>maxNo:
                maxNo=i
            lArr.append(maxNo)

        rArr = []
        maxNo = 0

        for i in range(len(height)-1,-1,-1):
            if height[i]>maxNo:
                maxNo= height[i]
            rArr.insert(0,maxNo)

        water = 0

        for i in range(len(height)):
            water+=(min(rArr[i], lArr[i])-height[i])

        return water




        