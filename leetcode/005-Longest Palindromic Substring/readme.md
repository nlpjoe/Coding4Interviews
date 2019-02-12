## 005-Longest Palindromic Substring

### 一、题目描述

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

```
Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

Example 3:

Input: "abb"
Output: "bb"
```

### 二、思路

#### 2.1 暴力算法

遍历一个字符串的所有子串时间复杂度为o(n^2)，验证一个子串是否回文时间复杂度为o(n)，总共时间o(n^3)。

一个思路是：如果减少子串回文验证时间？

#### 2.2 动态规划

每个位置的数，只可能构成长度为奇数和长度为偶数的回文。

- 长度为奇数，以自己为轴向两边散开
- 长度为偶数，以自己与后一个数(或前一个数)为轴向两边散开

在遍历的过程中，取最长的回文即为答案。

代码看起来似乎是子串遍历时间从o(n^2)降到了o(n)，但是实际上每个字母遍历的次数时间复杂度是o(2n)=o(n)的，只是在遍历的时候验证了子串是否是回文，因此时间复杂度相比于暴力法减少了o(n)的时间。总的时间复杂度为o(n^2)。




