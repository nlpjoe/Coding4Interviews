class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def GetNext(self, pNode):
        # write code here
        if not pNode: return None
        p = pNode
        if pNode.right:  # 有右子树
            p = pNode.right
            while p.left:
                p = p.left
            return p
         # 没有右子树但是有父亲节点
        while pNode.next and pNode.next.right == pNode:
            pNode = pNode.next
        return pNode.next