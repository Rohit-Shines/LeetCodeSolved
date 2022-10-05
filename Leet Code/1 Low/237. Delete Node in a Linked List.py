

class Solution:
    def deleteNode(self, node=[4,5,1,9]):
        node.val = node.next.val
        node.next = node.next.next

obj=Solution()
obj.deleteNode()