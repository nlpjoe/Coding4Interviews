### 题目描述

https://leetcode.com/problems/unique-paths/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
![](https://aigroupz-1258285787.cos.ap-shanghai.myqcloud.com/blog/15508034087703.jpg)
Above is a 7 x 3 grid. How many possible unique paths are there?

**Note:** m and n will be at most 100.

```
Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
```


### 思路

dp[i][j]表示从(0,0)到(i,j)的可到达数。

dp[i][j] = dp[i-1][j] + dp[i][j-1]