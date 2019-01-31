# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.index = -1

    def Serialize(self, root):
        # write code here
        if root:
            return str(root.val) + ' ' +\
                self.Serialize(root.left) + \
                self.Serialize(root.right)
        else:
            return '# '

    def Deserialize(self, s):
        # write code here
        l = s.split()
        self.index += 1
        if self.index >= len(s): 
            return None
        
        if l[self.index] != '#':
            root = TreeNode(int(l[self.index]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        else:
            return None
        return root


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


print(Solution().Serialize(root))
