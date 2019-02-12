class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        windows = []
        sum = 0
        for t in range(1, tsum):
            windows.append(t)
            sum += t
            while sum > tsum:
                sum -= windows.pop(0)
            if sum == tsum:
                res.append(windows[:])

        return res    

print(Solution().FindContinuousSequence(100))
        
