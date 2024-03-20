import pygame, random, sys

class microbe:
    def __init__(self, x, y, color, size, directions, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.directions = directions
        self.endurance = 100  # Initial endurance value

    def direction_from_genes(self, direction_index):
        return self.directions[direction_index]

    def move(self, size):
        if self.endurance > 0:  # Check if the microbe has endurance to move
            direction_index = random.randint(0, len(self.directions) - 1)
            dx, dy = self.direction_from_genes(direction_index)
            self.x = (self.x + dx) % size
            self.y = (self.y + dy) % size
            self.endurance -= 1  # Reduce endurance with each move

    def eat_food(self, food):
        if self.x == food.x and self.y == food.y:  # Check if the microbe is on the same position as the food
            self.endurance += 40  # Increase endurance by 40 when eating food

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))
