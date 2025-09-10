# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q=[]
        res=[]

        q.append(root)
        cur_levl=0

        while q:
            len_q = len(q)
            res.append([])

            for i in range(len_q):
                node = q.pop(0)
                if node:
                    res[cur_levl].append(node.val)

                
                    q.append(node.left)

                
                    q.append(node.right)

            if res[-1]==[]:
                res.pop()
            cur_levl+=1

        return res

        
        