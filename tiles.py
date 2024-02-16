import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/street.png")
        self.rect = self.image.get_rect(topleft = pos)