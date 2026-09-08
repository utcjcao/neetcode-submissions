# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        oq, nq = [], []
        if root:
            oq.append(root)
        storage = []
        while len(oq) > 0:
            level_storage = []
            for i in range(len(oq)):
                level_storage.append(oq[i].val)
                if oq[i].left:
                    nq.append(oq[i].left)
                if oq[i].right:
                    nq.append(oq[i].right)
            oq, nq = nq, []
                
            storage.append(level_storage)
        return storage
        