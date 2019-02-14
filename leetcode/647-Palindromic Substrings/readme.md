### 题目描述

https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

```
Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
```

Note:

The input string length won't exceed 1000.

### 思路

暴力遍历所有的子串o(n^2)复杂度，判断子串是否是回文o(n)复杂度，总共o(n^3)

直接的思路是降低子串回文判断的复杂度，总复杂度为o(n^2)

dp[i][j]表示i-j是否是回文，公式是：

dp[i][i] = True
dp[i][j] = dp[i+1][j-1] and f[i] == f[j]
