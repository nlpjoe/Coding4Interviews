### 题目链接

https://leetcode.com/problems/minimum-falling-path-sum/

Given a square array of integers A, we want the minimum sum of a falling path through A.

A falling path starts at any element in the first row, and chooses one element from each row.  The next row's choice must be in a column that is different from the previous row's column by at most one.

 
```
Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: 12
```

Explanation: 
The possible falling paths are:

- [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
- [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
- [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]

The falling path with the smallest sum is [1,4,7], so the answer is 12.

Note:

1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100



### 思路

我的一个直观算法是o(n^2)的时间和空间复杂度，dp公式如下：

dp[i][j] = f[i][j] + min(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])

讨论区的代码是在原数组上操作，节省o(n^2)的空间，但是会修改数组。