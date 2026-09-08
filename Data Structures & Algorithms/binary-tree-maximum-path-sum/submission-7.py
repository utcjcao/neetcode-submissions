# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # first intuition. we convert back to list, use kadanes
        # and we're gonna do it with pre order traversal
        # the issue. it ignores certain nodes that we have to travel to. 
        # is there a way to organize the nodes such that we still observe this property?
        # i think we can still use kadanes in a way. 
        # for any node, we have left and right. 
        # you can calcuate the node's max value by adding its val with the max val of its left and right
        # base case for a leaf, just return val.
        def traverse(node, m):
            # assume that traverse returns the total of max one path subtree,
            # and we calculate max of node as root independently (so not returned)
            if not node:
                return 0
            left, right = traverse(node.left, m), traverse(node.right, m)
            # case 1: i am center node
            total = node.val
            total += max(left, 0)
            total += max(right, 0)
            m[0]= max(m[0], total)
            # case 2: i am child node, and i can only pick one subtree to bring with me
            return max(node.val+left, node.val+right, node.val)        
        
        m = [float("inf") * -1]
        traverse(root,m)
        return m[0]
        
