# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        i = 0
        j = len(array[0])
        while(i<len(array) and j>=0):
            if target<array[i][j]:
                j -= 1
            elif target >array[i][j]:
                i += 1
            else:
                return True
        return False


