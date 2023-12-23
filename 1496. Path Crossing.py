class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        paths = {
            'N': [0, 1],
            'S': [0, -1],
            'E': [1, 0],
            'W': [-1, 0]
        }
        x , y = 0, 0
        visited = set()
        for move in path:
             visited.add((x, y))
             dx, dy = paths[move]
             (x, y) = (x + dx, y + dy)
             if (x, y) in visited:
                 return True
        return False
