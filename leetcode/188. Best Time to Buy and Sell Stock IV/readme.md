### 题目链接

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

```
Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
```

### 思路

T[i][k][0] 表示在第i个位置完成k次交易后手上持0股。
T[i][k][1] 表示在第i个位置完成k次交易后手上持1股。
本题中k = 任意值
在第i个位置有三种可能操作，买、卖、不动。故公式如下：

```
T[i][0][0] = 0
T[i][k][0] = max(T[i-1][k][0], T[i][k][1] + p)
T[i][k][1] = max(T[i-1][k][1], T[i][k-1][0] - p)
```

