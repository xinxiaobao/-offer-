# 将列表值存入数组，倒数k直接用数组指针
# 当 k == 0 时，返回None值
# 当 k 大于列表长度，也返回None值

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k == 0:
            return None
        res = []
        while head:
            res.append(head)
            head = head.next
        return res[-k] if len(res) >= k else None
