class Cell:
    def __init__(self, x, y, alive=False):
        self.x = x
        self.y = y
        self.alive = alive
        self.grid = None

    def __repr__(self):
        return f'Cell(row={self.x}, col={self.y}, alive={self.alive})'

    def is_alive(self):
        return self.alive

    def set_alive(self):
        self.alive = True

    def set_dead(self):
        self.alive = False

    def get_neighbours(self):
        neighbours = []

        for dx in [-1, 0, 1]:
            if 0 <= self.x + dx < self.grid.width:
                for dy in [-1, 0, 1]:
                    if 0 <= self.y + dy < self.grid.height:
                        if dx == 0 and dy == 0:
                            continue
                    
                        neighbours.append((self.x + dx, self.y + dy))

        return neighbours
