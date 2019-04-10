# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        self.attr = []
        if not pRootOfTree:
            return
        self.minorder(pRootOfTree)
        for i,v in enumerate(self.attr[:-1]):
            self.attr[i].right = self.attr[i+1]
            self.attr[i+1].left = self.attr[i]
        return self.attr[0]
    def minorder(self,root):
        if not root:
            return
        self.minorder(root.left)
        self.attr.append(root)
        self.minorder(root.right)