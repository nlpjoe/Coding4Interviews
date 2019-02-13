### 题目描述

https://leetcode.com/problems/counting-bits/

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

```
Example 1:

Input: 2
Output: [0,1,1]

Example 2:

Input: 5
Output: [0,1,1,2,1,2]
```

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

### 思路

暴力法O(n*sizeof(n))也能过，follow up中要求O(n)复杂度，需要用动态规划。
一个数的二进制数(假设为8位)，它为前7位数的1个数和最右位1的个数之和，比如考虑5中1的个数

5的二进制为：00000111
5的二进制数由5>>1的二进制数00000011 与 5%2=1的二进制数的和

故dp[i] = dp[i>>1] + i%2


