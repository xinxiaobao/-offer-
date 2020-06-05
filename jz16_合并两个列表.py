# 合成后的链表满足单调不减规则
# 构建一个链表pHead，每次对比pHead1.val 和 pHead2.val 将小的值加入pHead
# 如果有一个链表空了，则把另一个链表都加到pHead中

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        temp = ListNode(0)
        pHead = temp
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                temp.next = pHead1
                pHead1 = pHead1.next
            else:
                temp.next = pHead2
                pHead2 = pHead2.next
            temp = temp.next
        if pHead1:
            temp.next = pHead1
        else:
            temp.next = pHead2
        return pHead.next

