class Solution(object):
    def find_min_path(self, maze, origin, dest):
        self.m, self.n = len(maze), len(maze[0])
        self.MAX_DIST = self.m * self.n + 1
        visited = [[0] * self.n for _ in range(self.m)]

        self.dest = dest
        origin_i, origin_j = origin

        path = self.explore(maze, origin_i, origin_j, 0, visited)
        return path if path < self.MAX_DIST else -1

    def explore(self, maze, i, j, current_dist, visited):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or \
                visited[i][j] or '0' == maze[i][j]:
            return self.MAX_DIST

        if [i, j] == self.dest:
            return current_dist

        visited[i][j] = 1

        dist_min = min([
            self.explore(maze, i - 1, j, current_dist + 1, visited),
            self.explore(maze, i + 1, j, current_dist + 1, visited),
            self.explore(maze, i, j - 1, current_dist + 1, visited),
            self.explore(maze, i, j + 1, current_dist + 1, visited),
        ])

        visited[i][j] = 0

        return dist_min
