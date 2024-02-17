import pygame
from level import Level
from settings import WIDTH, HEIGHT, level_map

pygame.init()

BACKGROUND = (135, 206, 235)
SPEED = 5


clock: pygame.time.Clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
gepesz = pygame.image.load("graphics/characters/gepesz/frame_00_delay-0.05s.gif").convert_alpha()
gepesz_rect = gepesz.get_rect(center=(WIDTH / 2, HEIGHT / 2))
infos = pygame.image.load("graphics/characters/infos/run/run_000.png").convert_alpha()
infos_rect = infos.get_rect(center=(WIDTH / 2, HEIGHT / 2))
level: Level = Level(level_map, screen)


RUNNING: bool = True
while RUNNING:
    screen.fill(BACKGROUND)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #escape lenyomásakor kilép a játékból
            RUNNING = False

    # irányítás gépész
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and gepesz_rect.right <= WIDTH:
        gepesz = pygame.image.load("graphics/characters/gepesz/frame_00_delay-0.05s.gif")
        gepesz_rect.x += SPEED
    elif keys[pygame.K_LEFT] and gepesz_rect.left >= 0:
        gepesz_rect.x -= SPEED
    if keys[pygame.K_UP] and gepesz_rect.top >= 0:
        gepesz_rect.y -= SPEED
    elif keys[pygame.K_DOWN] and gepesz_rect.bottom <= HEIGHT:
        gepesz_rect.y+= SPEED

    # irányítás infós
    if keys[pygame.K_d] and infos_rect.right <= WIDTH:
        infos = pygame.image.load("graphics/characters/infos/run/run_000.png")
        infos_rect.x += SPEED
    elif keys[pygame.K_a] and infos_rect.left >= 0:
        infos_rect.x -= SPEED
    if keys[pygame.K_w] and infos_rect.top >= 0:
        infos_rect.y -= SPEED
    elif keys[pygame.K_s] and infos_rect.bottom <= HEIGHT:
        infos_rect.y+= SPEED


    level.run()
    screen.blit(gepesz, gepesz_rect)
    screen.blit(infos, infos_rect)
    pygame.display.update()
    clock.tick(60)

pygame.quit()