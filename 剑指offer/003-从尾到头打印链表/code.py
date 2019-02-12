
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法1：用辅助栈存储
def printListFromTailToHead(listNode):
    # write code here
    stack = []
    result_array = []
    node_p = listNode
    while node_p:
        stack.append(node_p.val)
        node_p = node_p.next 
    while stack:
        result_array.append(stack.pop(-1))
    return result_array


# 解法2：本身栈调用
result_array = []
def printListFromTailToHead(listNode):
    # write code here
    if listNode:
        printListFromTailToHead(listNode.next)
        result_array.append(listNode.val)
    return result_array
