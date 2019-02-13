class NumArray(object):
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0]*(len(nums)+1)
        for i in range(len(nums)):
            if i == 0:
                self.dp[i] = nums[i]
            else:
                self.dp[i] = self.dp[i-1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dp[j] - self.dp[i-1]
        


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))