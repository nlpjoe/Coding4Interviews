class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot: return 0
        queue = [pRoot]
        deep = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            deep += 1
        return deep
                