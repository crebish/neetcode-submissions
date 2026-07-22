# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, pLeft, pRight):
            if not node:
                return True

            if not (pLeft < node.val < pRight):
                return False

            return dfs(node.left, pLeft, node.val) and dfs(node.right, node.val, pRight)

        return dfs(root, float("-inf"), float("inf"))