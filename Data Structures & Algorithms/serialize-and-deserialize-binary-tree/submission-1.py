# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # initial thoughts. go thru list bfs style, serialize. 
        # deserialize by flling out tree dfs style. issue:
        # node vals can be bigger than 9, also can be negative. 
        # alternatively, have a string filled with 5 * n zeros, so there will always 
        # be enough space
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        s = []
        q = deque([root])
        while len(q) > 0:
            node = q.popleft()
            if node:
                new_s = str(node.val)
                s.append(new_s) 
                q.append(node.left)
                q.append(node.right)
            else:
                s.append("N")
        print(s)
        return ",".join(s)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        if vals[0] == "N": return None
        root = TreeNode(int(vals[0]))
        q = deque([root])
        index = 1
        while q:
            node = q.popleft()
            if vals[index] != "N":
                node.left = TreeNode(int(vals[index]))
                q.append(node.left)
            index += 1
            if vals[index] != "N":
                node.right = TreeNode(int(vals[index]))
                q.append(node.right)
            index += 1
        return root