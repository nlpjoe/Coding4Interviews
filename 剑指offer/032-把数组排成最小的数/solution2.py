import functools
def compare(s1, s2):
    if s1+s2 < s2+s1:
        return -1
    elif s1+s2 == s2+s1:
        return 0
    else:
        return 1

def PrintMinNumber(numbers):
    # write code here
    if not numbers: return ''
    if len(numbers) == 1: return numbers[0]
    str_numbers = [str(n) for n in numbers]

    return ''.join(sorted(str_numbers, key=functools.cmp_to_key(compare)))

print(PrintMinNumber([32, 3, 321]))
    
    
