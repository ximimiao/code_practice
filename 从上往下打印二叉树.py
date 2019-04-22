# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        result = []
        queue = []
        queue.append(root)
        while(len(queue)>0):
            index = queue.pop(0)
            result.append(index.val)
            if index.left:
                queue.append(index.left)
            if index.right:
                queue.append(index.right)
        return result