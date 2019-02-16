### 题目链接

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

```
Example 1:

Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

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
本题中k = 2
在第i个位置有三种可能操作，买、卖、不动。故公式如下：

```
T[i][0][0] = 0

T[i][1][0] = max(T[i-1][1][0], T[i-1][1][1] + p)
T[i][1][1] = max(T[i-1][1][1], T[i-1][0][0] - p)

T[i][2][0] = max(T[i-1][2][0], T[i-1][2][1] + p)
T[i][2][1] = max(T[i-1][2][1], T[i-1][1][0] - p)

```