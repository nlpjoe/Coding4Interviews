class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getDeep(x):
    if x is None:
        return 0
    return 1 + max(getDeep(x.left), getDeep(x.right))

class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return 1
        return abs(getDeep(pRoot.left)-getDeep(pRoot.right)) <= 1 \
                and IsBalanced_Solution(pRoot.left) \
                and IsBalanced_Solution(pRoot.right) 

