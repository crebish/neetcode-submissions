# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return (True, 0)

            b1, h1 = dfs(node.left)
            b2, h2 = dfs(node.right)

            if not b1 or not b2:
                return (False, 0)

            if abs(h1 - h2) > 1:
                return (False, 0)

            return (True, max(h1, h2) + 1)

        
        return dfs(root)[0]