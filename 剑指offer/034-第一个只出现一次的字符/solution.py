def FirstNotRepeatingChar(s):
    # write code here
    map = {}
    for i in range(len(s)):
        map[s[i]] = map.get(s[i], 0) + 1
    for i in range(len(s)):
        if map[s[i]] == 1:
            return i
    return -1

print(FirstNotRepeatingChar('abac'))