import random

class SimulatedEvolution:
    def __init__(self, width, height, cellsize, food_spawn_per_tick):
        self.width = width
        self.height = height
        self.cellsize = cellsize
        self.cells_x = int(width / cellsize)
        self.cells_y = int(height / cellsize)
        self.food_spawn_per_tick = food_spawn_per_tick
        self.food = [[0] * self.cells_y for _ in range(self.cells_x)]
        self.microbes = []

    def put_food(self, x, y):
        x_index = int(x)
        y_index = int(y)
        self.food[x_index][y_index] = 1

    def remove_food(self, x, y):
        self.food[x][y] = 0

    def spawn_food_normal(self):
        for _ in range(self.food_spawn_per_tick):
            x = random.randint(0, self.cells_x - 1)
            y = random.randint(0, self.cells_y - 1)
            self.put_food(x, y)

    def spawn_food_box(self):
        cx = self.cells_x / 2
        cy = self.cells_y / 2

        for _ in range(self.food_spawn_per_tick // 4):
            x = random.randint(0, self.cells_x - 1)
            y = random.randint(0, self.cells_y - 1)

            if abs(cx - x) > 100 or abs(cy - y) > 100:
                self.put_food(x, y)

        w = self.cells_x // 8
        h = self.cells_y // 8
        for _ in range(self.food_spawn_per_tick):
            x = cx + random.randint(-w // 2, w // 2)
            y = cy + random.randint(-h // 2, h // 2)
            self.put_food(x, y)

    def spawn_food_lines(self):
        for _ in range(self.food_spawn_per_tick // 10):
            x = random.randint(0, self.cells_x - 1)
            y = random.randint(0, self.cells_y - 1)
            self.put_food(x, y)

        cx = self.cells_x / 2
        cy = self.cells_y / 2
        w = self.cells_x / 6
        h = self.cells_y / 6

        for _ in range(self.food_spawn_per_tick // 2):
            x = random.randint(0, self.cells_x - 1)
            y = cy
            self.put_food(x, y)
            self.put_food(x, y + 50)
            self.put_food(x, y - 50)
            self.put_food(x, y + 100)
            self.put_food(x, y - 100)

            self.put_food(y, x)
            self.put_food(y + 50, x)
            self.put_food(y - 50, x)
            self.put_food(y + 100, x)
            self.put_food(y - 100, x)

    def spawn_food(self, strategy):
        if strategy == 0:
            self.spawn_food_normal()
        elif strategy == 1:
            self.spawn_food_lines()
        elif strategy == 2:
            self.spawn_food_box()

    def update_microbes(self, microbes):
        for microbe in self.microbes:
            microbe.move(self.width, self.height)
            x, y = microbe.x // self.cellsize, microbe.y // self.cellsize
            if self.food[x][y] == 1:
                self.remove_food(x, y)  # Supprimer la nourriture si le microbe la mange