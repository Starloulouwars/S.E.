import pygame
from read_colors import read_color_parameters

#setup
pygame.init()

#declarations
size = 800
fps = 30

#color
read = read_color_parameters()
read.readColors("color.ini")
color = read.c

#screen
screen = pygame.display.set_mode((size,size))
clock = pygame.time.Clock()
running = True
dt = 0

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
    
    pygame.display.flip()
    dt = clock.tick(fps)
    
pygame.quit()