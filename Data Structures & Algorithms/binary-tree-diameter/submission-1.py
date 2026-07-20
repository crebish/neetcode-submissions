# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):
            if not node:
                return (0, 0)

            l, ans1 = dfs(node.left)
            r, ans2 = dfs(node.right)

            return (max(l+1, r+1), max(ans1, ans2, l + r))

        _, ans = dfs(root)

        return ans