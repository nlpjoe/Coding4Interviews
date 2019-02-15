### 题目描述

https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

```
Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Example 2:
Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
```

Note:

0 < s1.length, s2.length <= 1000.
All elements of each string will have an ASCII value in [97, 122].

### 思路

和最大编辑距离不同的是本题只能删词，dp[i][j]表示s1[0..i]到s2[0..j]的最小代价，dp公式如下：

dp[i][j] = dp[i-1][j-1]                                         if f[i] == f[j]
dp[i][j] = min(dp[i][j-1]+W_del[j], dp[i-1][j] + W_del[i])      else

和discuss区方法相同