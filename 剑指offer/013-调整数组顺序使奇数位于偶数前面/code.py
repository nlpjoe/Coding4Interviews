def reOrderArray(array):
    # write code here
    odd_cnt = 0
    res = [0] * len(array)
    # 统计个数
    for n in array:  
        if n % 2 != 0:
            odd_cnt += 1
    # 填坑
    odd_i = 0
    even_i = odd_cnt
    for i in range(len(array)):
        if array[i] % 2 != 0:  
            res[odd_i] = array[i]
            odd_i += 1
        else:
            res[even_i] = array[i]
            even_i += 1
    return res
        

