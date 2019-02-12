class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        n_p1 = 0
        n_p2 = 0
        while p1:
            p1 = p1.next
            n_p1 += 1
        while p2:
            p2 = p2.next
            n_p2 += 1
        if n_p1 < n_p2:
            pHead1, pHead2 = pHead2, pHead1
        for _ in range(n_p1 - n_p2):
            pHead1 = pHead1.next
        while pHead1:
            if pHead1 == pHead2:
                return pHead1
            else:
                pHead1 = pHead1.next
                pHead2 = pHead2.next
        return None
