class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        columns = []
        negdig = []
        posdig = []
        result = []

        def solve(row):
            if row == n:
                result.append([''.join(['Q' if i == col else '.' for i in range(n)]) for col in columns])
                return  # Add the base case for backtracking

            for col in range(n):
                if col not in columns and row - col not in negdig and row + col not in posdig:
                    columns.append(col)
                    negdig.append(row - col)
                    posdig.append(row + col)
                    solve(row + 1)
                    columns.pop()
                    posdig.pop()
                    negdig.pop()

        solve(0)
        return result if result else []
