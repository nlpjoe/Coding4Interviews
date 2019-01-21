
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

### 前序遍历，深度优先遍历dfs
result_all = []
array = []
def FindPath(root, expectNumber):
    # write code here
    if not root: return []
    array.append(root.val)
    expectNumber -= root.val
    if expectNumber == 0 and not root.left and not root.right:
        result_all.append(array[:])
    FindPath(root.left, expectNumber)
    FindPath(root.right, expectNumber)
    array.pop()
    return result_all


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(4)
root.left.right = TreeNode(7)

print(FindPath(root, 19))
# print(FindPath(root, 15))