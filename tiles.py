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
class Barrier(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/barrier.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
class Activate(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/temp/water2.png")
        self.rect = self.image.get_rect(topleft = pos)

class Asztal(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/asztal.png")
        self.rect = self.image.get_rect(topleft = pos)

class Csempe(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/csempe.png")
        self.rect = self.image.get_rect(topleft = pos)
class Parketta(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/parketta.png")
        self.rect = self.image.get_rect(topleft = pos)

class Szék(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/szek.png")
        self.rect = self.image.get_rect(topleft = pos)

class Finished_check(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/street.png")
        self.rect = self.image.get_rect(topleft = pos)

class Ajtó(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/fobejarat.png")
        self.rect = self.image.get_rect(topleft = pos)


class Switch(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], switch_pic: str):
        super().__init__()
        self.image = pygame.image.load(switch_pic)
        self.rect = self.image.get_rect(topleft=pos)
    def update_image(self, switch_on):
        if switch_on:
            self.image = pygame.image.load("graphics/temp/switch_on.png")  
        else:
            self.image = pygame.image.load("graphics/temp/switch_off.png")

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.image = pygame.image.load("graphics/map/blocks/platform.png")
        self.rect = self.image.get_rect(topleft = pos)