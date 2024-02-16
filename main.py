import pygame

pygame.init()

WIDTH: int = 1900
HEIGHT: int = 1000
BACKGROUND = (135, 206, 235)
SPEED = 5

clock: pygame.time.Clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: #escape lenyomásakor kilép a játékból
            running = False

    screen.fill(BACKGROUND)
    pygame.display.update()
    clock.tick(60)

pygame.quit()