# https://leetcode.com/problems/rotting-oranges/
from typing import List
import collections


class Solution:
    '''
    In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.
    Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

    Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    If this is impossible, return -1 instead.  
    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2
    '''

    def get_steps_to_rot(self, grid: List[List[int]], grid_size, node_pos) -> int:
        '''
        from the start position, find the shortest path to a rotten orange
        '''
        (R, C) = grid_size
        (i, j) = node_pos

        def neighbors(r, c):
            for nr, nc in ((r-1, c), (r, c-1), (r+1, c), (r, c+1)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc

        visited = set()
        queue = collections.deque()
        visited.add((i, j))
        queue.append((i, j, 0))
        while queue:
            node_info = queue.popleft()
            i, j, d = node_info[0], node_info[1], node_info[2]
            for nr, nc in neighbors(i, j):
                if grid[nr][nc] == 2:  # we found a rotten orange!
                    return d+1
                # we keep traversing
                if not (nr, nc) in visited and grid[nr][nc] == 1:
                    visited.add((nr, nc))
                    queue.append((nr, nc, d+1))

        # we will be here if we can not find any rotten orange!
        return -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # for each fresh orange (value 1), do a BFS to find it's distance to a rotten orange,
        # the path shall only be another fresh orange (i.e. value 1)
        # if we can not find such a path, it means the orange will not rot.
        # We should also check that at the end, there are no fresh oranges left.
        R = len(grid)
        C = len(grid[0])

        max_steps = 0
        n_fresh_oranges = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    n_fresh_oranges += 1
                    steps_to_rot = self.get_steps_to_rot(grid, (R, C), (i, j))
                    if steps_to_rot == -1:
                        return -1  # i.e. no way to rot this orange.
                    if steps_to_rot > max_steps:
                        max_steps = steps_to_rot

        return max_steps
