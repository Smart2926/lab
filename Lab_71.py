class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = self.count_length(maze)
        self.cols = self.count_length(maze[0])
        self.visited = self.create_empty_grid(self.rows, self.cols)
        self.path = []

    def count_length(self, iterable):
        count = 0
        for _ in iterable:
            count += 1
        return count

    def create_empty_grid(self, rows, cols):
        grid = []
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append(False)
            grid.append(row)
        return grid

    def is_valid_move(self, x, y):
        if x < 0 or y < 0 or x >= self.rows or y >= self.cols:
            return False
        if self.maze[x][y] == 1 or self.visited[x][y]:
            return False
        return True

    def find_exit(self, x, y, end_x, end_y):
        if not self.is_valid_move(x, y):
            return False

        self.visited[x][y] = True
        self.path.append((x, y))

        if x == end_x and y == end_y:
            return True

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dx, dy in directions:
            if self.find_exit(x + dx, y + dy, end_x, end_y):
                return True

        self.path.pop()
        return False

    def solve(self, start_x, start_y, end_x, end_y):
        if self.find_exit(start_x, start_y, end_x, end_y):
            return self.path
        return None

maze = [
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 1, 0]
]

solver = MazeSolver(maze)
start_x, start_y = 0, 0
end_x, end_y = 4, 4
result = solver.solve(start_x, start_y, end_x, end_y)

if result:
    print("Шлях до виходу:", result)
else:
    print("Вихід не знайдено.")
