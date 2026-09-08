# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {inorder[i]: i for i in range(len(inorder))}
        if (len(preorder)) == 0: return 
        root = TreeNode(preorder[0])
        mid = inorder_map[preorder[0]]
        root.left = self.buildTree(preorder = preorder[1:mid+1], inorder=inorder[:mid])
        root.right = self.buildTree(preorder = preorder[mid+1:], inorder=inorder[mid+1:])
        return root