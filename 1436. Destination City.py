class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        destination = set()
        for path in paths:
            destination.add(path[1])
        for path in paths:
            if path[0] in destination:
                destination.remove(path[0])
        return destination.pop()
