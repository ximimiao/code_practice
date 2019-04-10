# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return 0
        if not pHead2:
            return 0
        length1 = self.GetLength(pHead1)
        length2 = self.GetLength(pHead2)
        lengthdiff = abs(length1-length2)
        if length1>length2:
            pHeadLong = pHead1
            pHeadshort = pHead2
        else:
            pHeadLong = pHead2
            pHeadshort = pHead1
        for i in range(lengthdiff):
            pHeadLong = pHeadLong.next
        while pHeadLong!=None and pHeadshort!=None and pHeadLong.val!=pHeadshort.val:
            pHeadLong = pHeadLong.next
            pHeadshort = pHeadshort.next
        return pHeadLong
    def GetLength(self,root):
        length = 0
        while root:
            root = root.next
            length += 1
        return length