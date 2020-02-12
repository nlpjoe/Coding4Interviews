### 前序遍历，深度优先遍历dfs
class Solution(object):
    def __init__(self):
        self.result_all = []
        self.array = []

    def pathSum(self, root, expectNumber):
        if not root: return []
        self.array.append(root.val)
        expectNumber -= root.val
        if expectNumber == 0 and not root.left and not root.right:
            self.result_all.append(self.array[:])
        self.pathSum(root.left, expectNumber)
        self.pathSum(root.right, expectNumber)
        self.array.pop()
        return self.result_all
