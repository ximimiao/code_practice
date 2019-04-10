# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        self.attr = []
        self.minorder(pRoot)
        if k<=0 or k>len(self.attr):
            return None
        else:
            return self.attr[k-1]
    def minorder(self,root):
        if not root:
            return None
        self.minorder(root.left)
        self.attr.append(root)
        self.minorder(root.right)