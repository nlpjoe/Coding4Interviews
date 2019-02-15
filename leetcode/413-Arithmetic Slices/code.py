class Solution1(object):
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        dp = [ [[0, 0] for _ in range(n)] for _ in range(n)]
        for i in range(n-2):
            if A[i+2] - A[i+1] == A[i+1] - A[i]:
                dp[i][i+2] = [1, A[i+1]-A[i]]
        for d in range(3, n):
            for i in range(n-d):
                if dp[i][i+d-1][0]:
                    dp[i][i+d][0] = dp[i][i+d-1][1] == (A[i+d] - A[i+d-1])
                    if dp[i][i+d][0]:
                        dp[i][i+d][1] = dp[i][i+d-1][1]
        cnt = 0
        for col in dp:
            for row in col:
                if row[0]: cnt += 1
        return cnt

class Solution2(object):
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        dp = [[None]*n for _ in range(n)]
        for i in range(n-2):
            if A[i+2] - A[i+1] == A[i+1] - A[i]:
                dp[i][i+2] = A[i+1]-A[i]

        for d in range(3, n):
            for i in range(n-d):
                if dp[i][i+d-1] is not None:
                    if dp[i][i+d-1] == (A[i+d] - A[i+d-1]):
                        dp[i][i+d] = dp[i][i+d-1]
        cnt = 0
        for col in dp:
            for row in col:
                if row is not None: cnt += 1
        return cnt

class Solution3(object):
    # from discuss
    def numberOfArithmeticSlices(self, A):
        n = len(A)
        curr = 0
        sum = 0
        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                curr += 1
                sum += curr
            else:
                curr = 0
        return sum
print(Solution3().numberOfArithmeticSlices([1, 1, 1, 1]))        
print(Solution3().numberOfArithmeticSlices([1, 2, 3, 4]))


