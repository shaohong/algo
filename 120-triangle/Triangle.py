from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # use DP.
        # DP[i][j] is the minimal path leading from triangle[0][0] to triangle[i][j]
        # DP state transition formula: DP[i][j]=min(DP[i-1][j], DP[i-1][j-1]) + triangle[i][j]
        DP = [[] for i in range(len(triangle))]
        # initialize the first row
        DP[0] = [triangle[0][0]]
        for i in range(1, len(triangle)):
            DP[i] = [-1] * (i+1)
            for j in range(0, i + 1):
                if j == 0:
                    DP[i][j] = DP[i-1][0] + triangle[i][0]
                elif j == i:
                    DP[i][j] = DP[i-1][j-1] + triangle[i][j]
                else:
                    DP[i][j] = min(DP[i-1][j], DP[i-1][j-1]) + triangle[i][j]


        return min(DP[len(triangle) - 1])


    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        # use DP.
        # DP[i][j] is the minimal path from bottom row to triangle[i][j]
        # DP state transition formula: DP[i][j]=min(DP[i+1][j], DP[i+1][j+1]) + triangle[i][j]
        # optimal solution is DP[0][0]
        n = len(triangle)
        DP = [[] for i in range(n)]

        # initialize the last row
        DP[n-1] = triangle[n-1]
        # start dynamic programming
        for i in range(n-2, -1, -1):
            DP[i] = [-1]* (i+1)
            for j in range(0, i+1):
                DP[i][j] = min(DP[i+1][j], DP[i+1][j+1]) + triangle[i][j]
        
        return DP[0][0]
