import pygame, random, sys
from read_colors import read_color_parameters
from microbe import microbe
from food import SimulatedEvolution

# Setup
pygame.init()

# Declarations
size = 800
width = 800
height = 800
cellsize = 2
food_spawn_per_tick = 10
fps = 60

# Color
read = read_color_parameters()
read.readColors("color.ini")
color = read.c

# Screen
screen = pygame.display.set_mode((size, size))
clock = pygame.time.Clock()
running = True
dt = 0

# Create microbes
num_microbes = 100
microbes = [microbe(random.randint(0, size - 1), random.randint(0, size - 1), color["microbe_color"], 3, [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)], screen) for _ in range(num_microbes)]

# Create an instance of the SimulatedEvolution class
simulation = SimulatedEvolution(width, height, cellsize, food_spawn_per_tick)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # Generate food
    simulation.spawn_food(strategy=0)  # Change strategy as needed

    # Move microbes, remove dead ones, and draw living ones
    alive_microbes = []
    for microbe in microbes:
        microbe.move(size)
        if microbe.is_alive():
            alive_microbes.append(microbe)
            microbe.draw()
            if microbe.try_replication():  # Check if microbe should replicate
                duplicate = microbe.replicate()  # Create a duplicate microbe
                alive_microbes.append(duplicate)  # Add the duplicate to the list of living microbes
    microbes = alive_microbes  # Update the list of microbes

    for x in range(simulation.cells_x):
        for y in range(simulation.cells_y):
            if simulation.food[x][y] == 1:
                pygame.draw.rect(screen, color["food_color"], (x * cellsize, y * cellsize, cellsize, cellsize))
                # Check if any microbe is touching the food
                for microbe in microbes:
                    if microbe.x // cellsize == x and microbe.y // cellsize == y:
                        simulation.remove_food(x, y)  # Remove food if a microbe is touching it

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
