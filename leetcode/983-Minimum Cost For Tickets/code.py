class Solution1(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        dp = [0] * 366
        for i in range(1, 366):
            if i in days:
                dp[i] = min(dp[max(i-1, 0)]+costs[0], dp[max(i-7, 0)]+costs[1], dp[max(i-30, 0)] + costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[365]

class Solution2(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        last7, last30 = [], []
        cost = 0
        for d in days:
            while last7 and last7[0][0] + 7 <= d:
                last7.pop(0)
            while last30 and last30[0][0] + 30 <= d:
                last30.pop(0)
            last7.append((d, cost+costs[1]))
            last30.append((d, cost+costs[2]))
            cost = min(cost+costs[0], last7[0][1], last30[0][1])
        return cost

print(Solution2().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))