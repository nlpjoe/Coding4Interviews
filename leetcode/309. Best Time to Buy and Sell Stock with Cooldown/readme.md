### 题目描述

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/#/description

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

- You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
- After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

```
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]
```

### 思路

T[i][k][0] 第i天买入k次并且手里持0股。
T[i][k][1] 第i天买入k次并且手里持1股。
k = 任意值并且有冷却期一天

如果第i天要买进，那么第i-1天必须休息不操作，那么T[i-1][k][0] = T[i-2][k][0]

公式如下：

T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + p)  # rest or sell
T[i][k][1] = max(T[i-1][k][1], T[i-2][k][0] - p)  # rest or buy



