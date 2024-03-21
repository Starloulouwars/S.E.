import pygame, random, sys, math
from food import SimulatedEvolution

class microbe:
    def __init__(self, x, y, color, size, directions, screen,):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.directions = directions
        self.endurance = 1500  # Initial endurance value
        self.last_direction = None

    def direction_from_genes(self):
        # Calculate probabilities for each direction
        probabilities = [random.random() for _ in range(len(self.directions))]
        total_prob = sum(probabilities)
        # Normalize probabilities to ensure they sum up to 1
        probabilities = [prob / total_prob for prob in probabilities]
        # Choose a direction based on probabilities
        direction_index = random.choices(range(len(self.directions)), weights=probabilities)[0]
        return self.directions[direction_index]

    def move(self, size):
        if self.endurance > 0:  # Check if the microbe has endurance to move
            if self.last_direction is None or random.random() < 0.1:  # Change direction occasionally
                self.last_direction = self.direction_from_genes()
            dx, dy = self.last_direction
            self.x = (self.x + dx) % size
            self.y = (self.y + dy) % size
            self.endurance -= 1  # Reduce endurance with each move

            # Decrease endurance for neighboring directions
            for direction in self.directions:
                if direction != self.last_direction:
                    distance = math.acos((direction[0] * dx + direction[1] * dy) / (math.sqrt(dx ** 2 + dy ** 2) * math.sqrt(direction[0] ** 2 + direction[1] ** 2)))
                    endurance_loss = 1
                    if distance > math.pi / 4:  # Increase endurance loss for directions farther from the current direction
                        endurance_loss *= 2
                    self.endurance -= endurance_loss


    def eat_food(self, food):
        if self.x == food.x and self.y == food.y:  # Check if the microbe is on the same position as the food
            self.endurance += 40  # Increase endurance by 40 when eating food
            print("miam")

    def try_replication(self):
        if self.endurance > 1000 and random.random() < 0.005:  # Check if endurance is greater than 1000 and chance of replication
            return True
        return False

    def replicate(self):
        duplicate = microbe(self.x, self.y, self.color, self.size, self.directions, self.screen)
        duplicate.endurance = self.endurance  # Le duplicata conserve la même endurance que l'original
        return duplicate

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.size, self.size))

    def is_alive(self):
        return self.endurance > 0
