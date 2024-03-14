import pygame

#setup
pygame.init()

#declarations
size = 800
fps = 30
font = pygame.font.Font('freesansbold.ttf', 20)

#color

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
                    
                    
                    
    screen.fill("#000000")
    
pygame.quit()