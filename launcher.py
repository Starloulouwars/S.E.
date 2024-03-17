import pygame, random, sys
from read_colors import read_color_parameters
from microbe import microbe

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

    pygame.display.flip()
    dt = clock.tick(fps)
    
pygame.quit()
sys.exit()