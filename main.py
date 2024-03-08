import pygame
from level import Level
from settings import WIDTH, HEIGHT, level_map_1, level_choice
from player import Gepesz
from infos import Infos
from enemy import Cigany


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

infos = Infos((WIDTH / 2, HEIGHT / 2 - 50))  
gepesz = Gepesz((WIDTH / 2, HEIGHT / 2))
cigany = Cigany((WIDTH / 2, HEIGHT / 2))



SPEED = 5


clock = pygame.time.Clock()
level = Level(screen, infos, gepesz, cigany)
BACKGROUND = pygame.image.load(level.background_image).convert() 

RUNNING = True
paused: bool = False
alive: bool = True
while RUNNING:    
    screen.blit(BACKGROUND, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
            if not paused:
                paused = True
            if paused:
                paused = False 
    alive = level.run(paused, alive)
    pygame.display.update()
    clock.tick(60)
