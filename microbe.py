import pygame, random, sys

class microbe:
    def __init__(self, x, y, color, size, direction, screen):
        self.screen = screen
        self.x = x
        self.y = y
        self.direction = direction  
        self.color = color
        self.size = size

    def move(self, size, direction):
        dx, dy = random.choice(direction)
        self.x = (self.x + dx) % size
        self.y = (self.y + dy) % size

    def draw(self, screen):
        screen.set_at((self.x, self.y), self.color)
