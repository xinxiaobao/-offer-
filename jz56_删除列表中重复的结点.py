
# 算法思路： 用列表存储链表， 列表中用filter过滤出，只出现一次的字符，重新构成链表返回

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        res = []
        while pHead:
            res.append(pHead.val)
            pHead = pHead.next
        res = list(filter(lambda x: res.count(x) == 1, res))
        ans = ListNode(0)
        pre = ans
        for i in res:
            node = ListNode(i)
            pre.next = node
            pre = pre.next
        return ans.next
        