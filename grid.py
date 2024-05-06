from cell import Cell

class Grid:
    def __init__(self, height, width, alive_cells):
        self.height = height
        self.width = width
        self.grid = [[Cell(x, y) for y in range(height)] for x in range(width)]
        self.alive_cells = alive_cells
        self.dead_cells = []
        for i in self.grid:
            for x in i:
                x.grid = self
        self.load_positions()

    def load_positions(self):
        for i in self.alive_cells:
            x, y = i
            self.grid[x][y].set_alive()

    def print_grid(self):
        grid_arr = []
        for i in range(self.width):
            row_string = ""
            for j in range(self.height):
                if self.grid[i][j].alive == True:
                    row_string += "#"
                else:
                    row_string += "_"
            grid_arr.append(row_string)

        for y in grid_arr:
            print(y)
        print()

    def update(self):
        current_positions = self.alive_cells
        all_neighbours = []
        new_alive_positions = set()

        for i in self.alive_cells[:]:
            x, y = i

            neighbours = self.grid[x][y].get_neighbours()
            all_neighbours.extend(neighbours)

            for j in neighbours[:]:
                x, y = j
                if not self.grid[x][y].is_alive() or j == i:
                    neighbours.remove(j)

            if len(neighbours) in [2, 3]:
                new_alive_positions.add(i)
        
        for i in all_neighbours[:]:
            x, y = i
            neighbours = self.grid[x][y].get_neighbours()
            for j in neighbours[:]:
                x, y = j
                if not self.grid[x][y].is_alive() or j == i:
                    neighbours.remove(j)
            
            if len(neighbours) == 3:
                new_alive_positions.add(i)

        self.alive_cells = list(new_alive_positions)
        self.dead_cells = [i for i in current_positions if i not in new_alive_positions]

        for i in current_positions:
            if i not in new_alive_positions:
                x, y = i
                self.grid[x][y].set_dead()

        self.load_positions()