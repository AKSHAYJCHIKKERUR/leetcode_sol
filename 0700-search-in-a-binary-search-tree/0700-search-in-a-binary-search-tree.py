# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        cur = root
        while cur:
            if target==cur.val:
                return cur
            elif target>cur.val:
                cur = cur.right
            else:
                cur = cur.left

        return None

 