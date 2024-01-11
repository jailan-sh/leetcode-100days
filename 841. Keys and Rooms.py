class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms)
        visited = set()
        keys = [0]
        while keys:
            room = keys.pop()
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    keys.append(key)
        return len(visited) == len(rooms)
