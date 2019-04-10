# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        pheadre = ListNode(0)
        phead = pheadre
        while pHead1 and pHead2:
            if pHead1.val <pHead2.val:
                phead.next = pHead1
                pHead1 = pHead1.next
            else:
                phead.next = pHead2
                pHead2 = pHead2.next
            phead = phead.next
        if pHead1:
            phead.next = pHead1
        elif pHead2:
            phead.next = pHead2
        return pheadre.next


