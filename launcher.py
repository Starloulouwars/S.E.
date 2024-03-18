import pygame, random, sys
from read_colors import read_color_parameters
from microbe import microbe
from food import SimulatedEvolution

#setup
pygame.init()

#declarations
size = 800
fps = 60

#color
read = read_color_parameters()
read.readColors("color.ini")
color = read.c

#screen
screen = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()
running = True
dt = 0

# Création de microbes
num_microbes = 1000
microbes = [microbe(random.randint(0, size - 1), random.randint(0, size - 1), color["microbe_color"], 1, [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)], screen) for _ in range(num_microbes)]

# Création d'une instance de la classe SimulatedEvolution
simulation = SimulatedEvolution({
    "cv": {
        "width": size,
        "height": size
    },
    "cellsize": 2,
    "food_spawn_per_tick": 1
})

running = True
pause = False
while running:
    for event in pygame.event.get():
    #keys
        if event.type == pygame.QUIT:
                running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                    
        
                    
    screen.fill(color["ground_color"])
    
    # Déplacement et dessin de chaque microbe
    for microbe in microbes:
        microbe.move(size, [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)])
        microbe.draw(screen)
        
    # Appel de la méthode spawn_food de l'instance de SimulatedEvolution
    simulation.spawn_food(strategy=0)
    
    ## Dessin de la nourriture
    for x in range(simulation.cells_x):
        for y in range(simulation.cells_y):
            if simulation.food[x][y] == 1:
                pygame.draw.rect(screen, (255, 255, 255), (x * simulation.cfg["cellsize"], y * simulation.cfg["cellsize"], simulation.cfg["cellsize"], simulation.cfg["cellsize"]))


    pygame.display.flip()
    dt = clock.tick(fps)
    
pygame.quit()
sys.exit()