# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        attr = [1]
        t2, t3, t5 = 0, 0, 0
        tempindex = 1
        while tempindex < index:
            minnum = min([attr[t2] * 2, attr[t3] * 3, attr[t5] * 5])
            attr.append(minnum)
            while (minnum >= attr[t2] * 2):
                t2 += 1
            while (minnum >= attr[t3] * 3):
                t3 += 1
            while (minnum >= attr[t5] * 5):
                t5 += 1
            tempindex += 1
        return attr[tempindex - 1]

# write code here
