# ref: https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    # the possible move to neighbour grids
    def __init__(self):
        self.moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def shallBeColored(self, grid: List[List[str]], i, j):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == '1'

    def setToZero(self, grid: List[List[str]], i, j):
        if self.shallBeColored(grid, i, j):
            grid[i][j] = '0'
            for m in self.moves:
                self.setToZero(grid, i+m[0], j+m[1])

    def numIslands(self, grid: List[List[str]]) -> int:
        # floodfill：iterate through the grid, if we find a '1', count++ and use DFS to set all neighbouring '1's to be '0'
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.setToZero(grid, i, j)
        return count


class UnionAndFind:
    def __init__(self, grid: List[List[str]]):
        # initialize the UnF, all notes point to itself as parent
        n_rows = len(grid)
        n_columns = len(grid[0])
        self.parent = [-1 for _ in range(n_rows * n_columns)]
        self.numberOfRoots = 0
        for i in range(n_rows):
            for j in range(n_columns):
                if grid[i][j] == '1':
                    self.parent[i * n_columns + j] = i * n_columns + j
                    self.numberOfRoots += 1

    def findRoot(self, i):
        ''' find the root of node i '''
        if self.parent[i] == i:
            return i

        root = self.findRoot(self.parent[i])
        # path compression
        self.parent[i] = root
        return root

    def union(self, i, j):
        root_i = self.findRoot(i)
        root_j = self.findRoot(j)
        if root_i == root_j:
            return

        # for all of root_i's children (including root_i itself), let root_j be their parent.
        for i, pid in enumerate(self.parent):
            if pid == root_i:
                self.parent[i] = root_j
        self.numberOfRoots -= 1

    def dumpRoots(self):
        roots = set()
        for i, _ in enumerate(self.parent):
            root_id = self.findRoot(i)
            if root_id >= 0:
                roots.add(root_id)
        print(f"{self.numberOfRoots} : {roots}")


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        # floodfill：iterate through the grid,
        # if we find a '1', count++ and use DFS to set all neighbouring '1's to be '0'
        if not grid or not grid[0]:
            return 0
        n_rows = len(grid)
        n_columns = len(grid[0])
        unf = UnionAndFind(grid)

        for i in range(n_rows):
            for j in range(n_columns):
                # if a node is '1', union it to it's left or top neighbours, if they are also '1'
                if grid[i][j] == '1':
                    # check top neighbour and do the union if needed
                    if i-1 >= 0 and grid[i-1][j] == '1':
                        unf.union(i*n_columns + j, (i-1)*n_columns + j)
                    # check left neighbour, and do the union if needed
                    if j-1 >= 0 and grid[i][j-1] == '1':
                        unf.union(i*n_columns + j, i*n_columns + j-1)

        return unf.numberOfRoots
