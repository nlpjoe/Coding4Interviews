### 题目描述

题目链接：https://leetcode.com/problems/min-cost-climbing-stairs/

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

```
Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
```

### 思路

挺有意思的easy题。斐波那契数列变形题，以后我做面试官可能会考虑考虑这个题。

第n个位置可以通过第n-1和第n-2到达，因此动态规划公式为：
dp(0) = 0
dp(1) = 0
dp(n) = min(dp(n-1)+f(n-1), dp(n-2)+f(n-2))


