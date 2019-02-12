
def find(target, array):
    i = 0
    j = len(array[0]) - 1
    while i < len(array) and j >= 0:
        base = array[i][j]
        if target == base:
            return True
        elif target > base: 
            i += 1
        else:
            j -= 1
    return False

print(find(4,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))