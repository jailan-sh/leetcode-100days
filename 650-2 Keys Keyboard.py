class Solution:
    def minSteps(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        operations = 0
        factor = 2

        while factor * factor <= n:
            if n % factor == 0:
                operations += factor
                n //= factor
            else:
                factor += 1
        if n > 1:
            operations += n

        return operations 
