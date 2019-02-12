
def Convert(pRootOfTree):
    if not pRootOfTree: return None
    stack = []
    p = pRootOfTree
    new_h = None
    pre = None
    while p or stack:
        while p:
            stack.append(p)
            p = p.left

        p = stack.pop()
        if not pre:
            pre = p
            new_h = p
        else:
            pre.right = p
            p.left = pre
            pre = p

        p = p.right
    return new_h


def Convert(pRootOfTree):
    if not pRootOfTree: return None
    return new_h


