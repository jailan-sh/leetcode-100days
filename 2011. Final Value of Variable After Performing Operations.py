class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        count = 0
        for op in operations:
            if "+" in op:
                count += 1
            elif "-" in op:
                count -= 1
        return count
