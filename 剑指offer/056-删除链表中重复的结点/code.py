class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        head = ListNode(0)
        head.next = pHead
        pre = head
        p = head.next
        while p and p.next:
            if p.next.val == p.val:
                while p.next and p.next.val == p.val:
                    p.next = p.next.next
                pre.next = p.next
                p = pre.next
            else:
                pre = p
                p = p.next
        return head.next