# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def rightDFS(node, level):
            if not node: 
                return

            if level > len(ans):
                ans.append(node.val)

            rightDFS(node.right, level + 1)
            rightDFS(node.left, level + 1)



        rightDFS(root, 1)
        return ans