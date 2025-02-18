import tkinter as tk
import random

# Define some colors
BLACK = "#000000"
WHITE = "#FFFFFF"
GRAY = "#808080"

GRID_WIDTH = 10
GRID_HEIGHT = 20
BLOCK_SIZE = 20

class Shape:
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.blocks = []

    def move_down(self, grid):
        if self.y + len(self.blocks) >= len(grid):
            return False
        for i, row in enumerate(self.blocks):
            for j, val in enumerate(row):
                if val and grid[self.y + i + 1][self.x + j]:
                    return False
        self.y += 1
        return True

    def move_side(self, dx, grid):
        if self.x + len(self.blocks[0]) >= len(grid[0]) and dx == 1:
            return
        if self.x <= 0 and dx == -1:
            return
        for i, row in enumerate(self.blocks):
            for j, val in enumerate(row):
                if val and (self.x + j + dx < 0 or self.x + j + dx >= len(grid[0]) or grid[self.y + i][self.x + j + dx]):
                    return
        self.x += dx

class IShape(Shape):
    def __init__(self):
        super().__init__()
        self.blocks = [[1, 1, 1, 1]]

class JShape(Shape):
    def __init__(self):
        super().__init__()
        self.blocks = [[1, 0, 0], [1, 1, 1]]

class LShape(Shape):
    def __init__(self):
        super().__init__()
        self.blocks = [[0, 0, 1], [1, 1, 1]]

class OShape(Shape):
    def __init__(self):
        super().__init__()
        self.blocks = [[1, 1], [1, 1]]

class SShape(Shape):
    def __init__(self):
        super().__init__()
        self.blocks = [[0, 1, 1], [1, 1, 0]]

class TShape(Shape):
    def __init__(self):
        super().__init__()
        self.blocks = [[0, 1, 0], [1, 1, 1]]

class ZShape(Shape):
    def __init__(self):
        super().__init__()
        self.blocks = [[1, 1, 0], [0, 1, 1]]

shapes = [IShape, JShape, LShape, OShape, SShape, TShape, ZShape]

class TetrisGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tetris")
        self.geometry(f"{GRID_WIDTH * BLOCK_SIZE}x{GRID_HEIGHT * BLOCK_SIZE}")
        self.canvas = tk.Canvas(self, width=GRID_WIDTH * BLOCK_SIZE, height=GRID_HEIGHT * BLOCK_SIZE, bg=BLACK)
        self.canvas.pack()
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.shape = random.choice(shapes)()
        self.score = 0
        self.bind("<Left>", self.move_left)
        self.bind("<Right>", self.move_right)
        self.bind("<Down>", self.move_down)
        self.update_game()

    def move_left(self, event):
        self.shape.move_side(-1, self.grid)
        self.update_canvas()

    def move_right(self, event):
        self.shape.move_side(1, self.grid)
        self.update_canvas()

    def move_down(self, event):
        self.shape.move_down(self.grid)
        self.update_canvas()

    def update_game(self):
        if not self.shape.move_down(self.grid):
            for i, row in enumerate(self.shape.blocks):
                for j, val in enumerate(row):
                    if val:
                        self.grid[self.shape.y + i][self.shape.x + j] = 1

            lines_cleared = 0
            for i, row in enumerate(self.grid):
                if all(row):
                    del self.grid[i]
                    self.grid.insert(0, [0 for _ in range(GRID_WIDTH)])
                    lines_cleared += 1
            self.score += lines_cleared ** 2

            self.shape = random.choice(shapes)()

        self.update_canvas()
        self.after(500, self.update_game)

    def update_canvas(self):
        self.canvas.delete("all")
        for i, row in enumerate(self.grid):
            for j, val in enumerate(row):
                if val:
                    self.draw_block(j, i, GRAY)
        for i, row in enumerate(self.shape.blocks):
            for j, val in enumerate(row):
                if val:
                    self.draw_block(self.shape.x + j, self.shape.y + i, self.shape.color)

    def draw_block(self, x, y, color):
        x1 = x * BLOCK_SIZE
        y1 = y * BLOCK_SIZE
        x2 = x1 + BLOCK_SIZE
        y2 = y1 + BLOCK_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=BLACK)

if __name__ == "__main__":
    game = TetrisGame()
    game.mainloop()
