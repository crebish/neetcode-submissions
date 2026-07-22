# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q or not root:
            return None

        def dfs(node):
            if not node:
                return None

            if node.val > max(p.val, q.val):
                return dfs(node.left)
            elif node.val < min(p.val, q.val):
                return dfs(node.right)
            else:
                return node


        return dfs(root)