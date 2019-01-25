def getDeep(x):
    if x is None:
        return 0
    left = getDeep(x.left)
    if left == -1:
        return -1
    right = getDeep(x.right)
    if right == -1:
        return -1
    return -1 if abs(left-right) > 1 else 1 + max(left, right)


class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return getDeep(pRoot) != -1
