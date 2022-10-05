def preorderTraversal(self, root=[1,null,2,3]):
    stack = [root]
    res = []
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    print(res)
    return

obj = Solution()
obj.preorderTraversal()