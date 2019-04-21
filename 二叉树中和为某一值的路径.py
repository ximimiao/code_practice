# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        result = []
        def Findpath2(root,path,currentnum):
            currentnum += root.val
            path.append(root)
            flag = root.left==None and root.right==None
            if currentnum==expectNumber and flag:
                onenode = []
                for node in path:
                    onenode.append(node.val)
                result.append(onenode)
            if currentnum<expectNumber:
                if root.left:
                    Findpath2(root.left,path,currentnum)
                if root.right:
                    Findpath2(root.right,path,currentnum)
            path.pop()
        Findpath2(root,[],0)
        return sorted(result,key=lambda i:len(i),reverse=True)
s = Solution()

node_2 = TreeNode(2)
node_2.left = TreeNode(4)
node_2.right= TreeNode(5)

node_3 = TreeNode(3)
node_3.left = TreeNode(6)
node_3.right= TreeNode(7)

node_1 = TreeNode(1)
node_1.left = node_2
node_1.right= node_3


res = s.FindPath(node_1, 8)
print(res)