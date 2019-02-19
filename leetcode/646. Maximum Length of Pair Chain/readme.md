## 题目描述

https://leetcode.com/problems/maximum-length-of-pair-chain/

You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

```
Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
Note:
The number of given pairs will be in the range [1, 1000].
```

## 思路

1. 按照元素第0位排序

dp[init] = 1

for i in range 0...n:
    for j in 0...i:
        dp[i] = max(dp[i], dp[j]+1 if A[j][1]<A[i][0])

