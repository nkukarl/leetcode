# TODO: Fix this!
class Solution(object):
    def find_min_path(self, maze, xa, ya, xb, yb):
        self.maze, self.m, self.n = maze, len(maze), len(maze[0])
        self.xb, self.yb = xb, yb
        self.visited = [[0] * self.n for _ in range(self.m)]
        self.min_steps = self.m * self.n
        self.path = None
        self.search(xa, ya, 0, [])
        print(self.path)
        return self.min_steps

    def search(self, x, y, steps, path):
        if x == self.xb and y == self.yb:
            if steps < self.min_steps:
                self.path = path
                self.min_steps = steps
            return
        if self.maze[x][y] == '0' or self.visited[x][y] == 1:
            return
        self.visited[x][y] = 1

        if x < self.m - 1:
            self.search(x + 1, y, steps + 1, path + [(x + 1, y)])
        if x > 0:
            self.search(x - 1, y, steps + 1, path + [(x - 1, y)])
        if y > 0:
            self.search(x, y - 1, steps + 1, path + [(x, y - 1)])
        if y < self.n - 1:
            self.search(x, y + 1, steps + 1, path + [(x, y + 1)])
