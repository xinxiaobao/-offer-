# 算法思路： 用list收集结点，当遇到重复结点，则说明该结点为中环入口结点


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        lis = []
        while pHead:
            if pHead in lis:
                return pHead
            lis.append(pHead)
            pHead = pHead.next
        return None