
### 题目描述

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
```
Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

### 思路

T[i][k][0] 表示在第i个位置完成k次交易后手上持0股。
T[i][k][1] 表示在第i个位置完成k次交易后手上持1股。
本题中k = +Infinity
在第i个位置有三种可能操作，买、卖、不动。故公式如下：

T[-1][k][0] = 0, T[-1][k][1] = -1
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])  # r or sell
T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])  # r or buy

