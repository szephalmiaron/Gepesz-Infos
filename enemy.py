import pygame

class Cigany(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()

        self.image = pygame.image.load("graphics/characters/cigany_uveggel.png")
        self.rect = self.image.get_rect(topleft = pos)
        self.frame_index: float = 0
        self.direction = pygame.math.Vector2(0,0)
        self.speed: int = 1
        self.facing_left: bool = False
