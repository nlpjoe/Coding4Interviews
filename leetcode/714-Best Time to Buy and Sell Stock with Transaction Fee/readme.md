### 题目描述

https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

```
Example 1:
Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
```

Note:

```
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
```

### 思路

此题与122一样，只是出售时需要多加个手续费。
T[i][k][0] 表示在第i个位置完成k次交易后手上持0股。
T[i][k][1] 表示在第i个位置完成k次交易后手上持1股。
本题中k = +Infinity
在第i个位置有三种可能操作，买、卖、不动。故公式如下：

T[-1][k][0] = 0, T[-1][k][1] = -1
T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i] - fee)  # r or sell
T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])  # r or buy
