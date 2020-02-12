# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.pre = None
        
    def Convert(self, root):
        # write code here
        if not root: return None
        self.helper(root)
        while root.left:
            root = root.left
        return root

    def helper(self, cur):
        if not cur: return None
        self.helper(cur.left)
        cur.left = self.pre
        if self.pre:
            self.pre.right = cur
        self.pre = cur
        self.helper(cur.right)
        
