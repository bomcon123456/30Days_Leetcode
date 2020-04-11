# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        res = 1
        def helper(node):
            nonlocal res
            if not node: return 0
            L = helper(node.left)
            R = helper(node.right)
            res = max(res, L+R+1)
            return max(L, R) + 1
        helper(root)
        return res-1