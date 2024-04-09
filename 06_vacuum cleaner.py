import random
class VacuumCleaner:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.position = (random.randint(0, rows-1), random.randint(0, cols-1))
        self.grid = [[random.choice([True, False]) for _ in range(cols)] for _ in range(rows)]

    def print_grid(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.position == (i, j):
                    print("V" if self.grid[i][j] else "V", end=" ")  # Vacuum cleaner symbol
                else:
                    print("D" if self.grid[i][j] else "-", end=" ")  # Dirt symbol
            print()

    def clean(self):
        cleaned = 0
        total_dirt = sum(row.count(True) for row in self.grid)
        while cleaned < total_dirt:
            if self.grid[self.position[0]][self.position[1]]:
                self.grid[self.position[0]][self.position[1]] = False  # Clean the dirt
                cleaned += 1
            self.print_grid()
            move_direction = input("Enter direction to move (up/down/left/right): ")
            self.move(move_direction)  # Corrected line to call move method with input direction
        print("All dirt cleaned!")

    def move(self, direction):
        if direction == "up" and self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])
        elif direction == "down" and self.position[0] < self.rows - 1:
            self.position = (self.position[0] + 1, self.position[1])
        elif direction == "left" and self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)
        elif direction == "right" and self.position[1] < self.cols - 1:
            self.position = (self.position[0], self.position[1] + 1)

rows=int(input("Enter no of rows:"))
columns=int(input("Enter no of columns:"))
vacuum = VacuumCleaner(rows,columns)
print("Initial grid:")
vacuum.clean()
