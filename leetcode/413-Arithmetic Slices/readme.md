### 题目链接

https://leetcode.com/problems/arithmetic-slices/

A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequence:
```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```
The following sequence is not arithmetic.
```
1, 1, 2, 5, 7
```
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:
```
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
```

### 思路

求一个数列的子数列是等差数列的数目。

这题和DP647比较像。遍历所有的子串需要的复杂度是o(n^2)，判断一个子串是否是等差数列时间复杂度是o(n)。

所以本题的思路是通过动态规划打表降低等差数列的判断时间为o(1)，动态规划公式如下：

#### 思路1 直接思路，爆内存了
dp[i][j][0] = True if f(j)-f(i)是等差数列                            j-i=1

dp[i][j][0] = dp[i][j-1][0] and f[j]-f[j-1] == dp[i][j-1][1]       j-i>2
if dp[i][j][0]: dp[i][j][1] = dp[i][j-1][1]

#### 思路2

把bool标记删减掉就好了，明天看看discuss看看别人的思路。

#### 思路3

牛逼的discuss思路，用curr表示第0~i个位置有多少个等差数列，求和即可。O(n)空间复杂度，O(1)时间复杂度。
