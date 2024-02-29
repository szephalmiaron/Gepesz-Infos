import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/street.png")
        self.rect = self.image.get_rect(topleft = pos)
class Water(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/temp/water2.png")
        self.rect = self.image.get_rect(topleft = pos)

class Lift(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/temp/lift.png")
        self.rect = self.image.get_rect(topleft = pos)
class Button(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/temp/button.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
class Switch(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/temp/switch_off.png")
        self.rect = self.image.get_rect(topleft = pos)