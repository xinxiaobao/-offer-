# 算法思路：两条相交的链表呈Y型。可以从两条链表尾部同时出发，最后一个相同的结点就是链表的第一个相同的结点。
#         分别遍历两个链表，将节点保存到 两个数组中，再分别pop两个数组，如果找到第一对不相同的节点，那么直接返回上一个节点即可。

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        
        stack1, stack2 = [], []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
        res = None
        while stack1 and stack2:
            p1 = stack1.pop()
            p2 = stack2.pop()
            if p1 == p2:    
                res = p1
            else:
                break
        return res

        

            