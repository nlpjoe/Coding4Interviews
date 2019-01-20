

def Mirror(root):
    # write code here
    if not root:
        return None
    tmp = Mirror(root.right)
    root.right = Mirror(root.left)
    root.left = tmp
    return root