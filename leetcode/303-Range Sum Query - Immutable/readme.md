### 题目描述
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

```
Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

Note:
You may assume that the array does not change.
There are many calls to sumRange function.


### 思路

dp[i]表示从0到i的sum

i到j的sum=dp[j]-dp[i]