class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers: return 0
        numbers.sort()
        cnt = 0
        jokers = 0
        pre = None
        for i in range(len(numbers)):
            if numbers[i] == 0:
                jokers += 1
            else:
                if pre is None:
                    pre = numbers[i]
                else:
                    if pre == numbers[i]: return 0
                    cnt += numbers[i] - pre - 1
                    pre = numbers[i]
        cnt -= jokers
        return cnt <= 0

print(Solution().IsContinuous([0,3,1,6,4]))