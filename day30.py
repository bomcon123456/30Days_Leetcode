class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.checkPath(root, arr, 0)

    def checkPath(self, root, arr, index):
        if root is None or index == len(arr):
             return False
            
        if root.left is None and root.right is None and root.val == arr[index] and index == len(arr)-1:
            return True
       
        return root.val == arr[index] and (self.checkPath(root.left, arr, index+1) or self.checkPath(root.right, arr, index+1))

