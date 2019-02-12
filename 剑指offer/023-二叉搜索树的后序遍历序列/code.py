def helper(sequence):
    if len(sequence) <= 1: return True
    root = sequence[-1]
    for i in range(len(sequence)):
        if sequence[i] > root:
            break
    for j in range(i, len(sequence)-1):
        if sequence[j] < root:
            return False
    return helper(sequence[:i]) and helper(sequence[i:-1])


def VerifySquenceOfBST(sequence):
    # write code here
    if not sequence: return False
    return helper(sequence)
print(VerifySquenceOfBST([7,4,6,5]))