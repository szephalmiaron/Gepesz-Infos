import pygame
from level import Level
class Cigany(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()
        self.image = pygame.image.load("graphics/characters/cigany_uveggel.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.frame_index: float = 0
        self.direction = pygame.math.Vector2(0,0)
        self.speed: int = 5

    def change_image(self, facing_left):
        if facing_left is False:
            self.image = pygame.image.load("graphics/characters/cigany_uveggel.png").convert_alpha()
        elif facing_left:
            self.image = pygame.transform.flip(pygame.image.load("graphics/characters/cigany_uveggel.png").convert_alpha(), True, False)

    def save_original_pos(self, pos):
        self.original_pos = pos