### 题目描述

https://leetcode.com/problems/count-numbers-with-unique-digits/

Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99

### 思路

设f(n)表示n位数有多少个不同数，则

f(1) = 10  明显
f(2) = 9 * 9  第一位i不为0，第二位j不同于i，分别为9。
f(3) = f(2) * 8  已有两位不同数，第三位k不同于i和j，k取值为8种。
f(4) = f(3) * 7 同理于f(3)
... ...
f(10) = f(9) * 1
f(11) = 0


