class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        queue = [pRoot]
        res = []
        while queue:
            n = len(queue)
            temp = []
            for _ in range(n):
                node = queue.pop(0)
                temp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp)
        return res
                