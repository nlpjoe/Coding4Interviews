class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def helper(treeA, treeB):
    if not treeB:
        return True
    elif not treeA:
        return False
    elif treeA.val != treeB.val:
        return False
    else:
        return helper(treeA.left, treeB.left) and helper(treeA.right, treeB.right)


def HasSubtree(pRoot1, pRoot2):
    # write code here
    if not pRoot1 or not pRoot2: return False
    # 2 是不是 1的子树
    res = False
    if pRoot1.val == pRoot2.val:
        res = helper(pRoot1, pRoot2)
    if res: 
        return True
    else:
        return HasSubtree(pRoot1.left, pRoot2) or HasSubtree(pRoot1.right, pRoot2)
        

    

