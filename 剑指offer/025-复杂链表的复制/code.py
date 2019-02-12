class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


# 返回 RandomListNode
def Clone(pHead):
    # write code here
    if not pHead: return None
    p = pHead
    new_h = RandomListNode(p.label)
    pre_p = new_h
    random_map = {pHead: new_h}
    p = p.next
    while p:
        new_p = RandomListNode(p.label)
        random_map[p] = new_p
        pre_p.next = new_p
        pre_p = pre_p.next
        p = p.next
    p = pHead
    new_p = new_h
    while p:
        random_p = p.random
        if random_p:
            new_p.random = random_map[random_p]

        p = p.next
        new_p = new_p.next

    return new_h

p = RandomListNode(1)
p.next = RandomListNode(2)
p.next.next = RandomListNode(3)
p.next.next.next = RandomListNode(4)
p.next.next.next.next = RandomListNode(5)
print(Clone(p))