class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        head = ListNode(0)
        head.next = pHead
        fast = head
        slow = head
        while True:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None
            if fast == slow:
                fast = head
                break
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast