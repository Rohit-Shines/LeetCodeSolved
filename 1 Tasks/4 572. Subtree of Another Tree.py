class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root=[3,4,5,1,2], subRoot=[4,1,2]):

        def check(root, subRoot, original):
            if not root and not subRoot:
                return True
            elif root and not subRoot:
                return False
            elif not root and subRoot:
                return False
            elif root.val != subRoot.val:
                return check(root.left, original, original) or \
                       check(root.right, original, original)
            elif root.val == subRoot.val:
                return (check(root.left, subRoot.left, original) and check(root.right, subRoot.right, original)) or \
                       (check(root.left, original, original) or check(root.right, original, original))

        return check(root, subRoot, subRoot)

obj =Solution()
TreeNode()
obj.isSubtree()