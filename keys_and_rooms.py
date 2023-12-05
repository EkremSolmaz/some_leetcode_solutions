from typing import List


class Solution:
    def visitRoom(self, rooms, i,  visited):
        if visited.get(i, False):
            return
        visited[i] = True
        for key in rooms[i]:
            self.visitRoom(rooms, key, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        self.visitRoom(rooms, 0, visited)

        return len(visited) == len(rooms)
