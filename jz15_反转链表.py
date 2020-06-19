# 当链表为空或者链表只有一个值，返回链表本身
# 算法逻辑： 从头开始，一个结点一个结点的调转结果，直到都调转


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pre = None
        cur = pHead
        while cur:
            aft = cur.next
            cur.next = pre
            pre = cur
            cur = aft
        return pre
