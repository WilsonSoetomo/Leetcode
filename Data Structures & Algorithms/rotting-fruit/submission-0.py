class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh_fruit = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                if grid[r][c] == 1:
                    fresh_fruit += 1

        distance = 0
        while q and fresh_fruit > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]\

                for dr, dc in directions:
                    row, col = dr + r, dc + c

                    if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh_fruit -= 1

            time += 1

        return time if fresh_fruit == 0 else -1
    