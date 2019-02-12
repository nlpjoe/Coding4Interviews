def PrintFromTopToBottom(root):
    # write code here
    if not root: return []
    queue = [root]
    res = []
    while queue:
        n = len(queue)
        for _ in range(n):
            if not queue: break
            node = queue.pop(0)
            res.append(node.val)
            if node.left:             
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res
