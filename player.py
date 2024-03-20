from typing import List
import pygame

class Gepesz(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()

        self.image = pygame.image.load("graphics/temp/gepesz/gepeszanimacio1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_index: float = 0
        self.direction = pygame.math.Vector2(0, 0)
        self.speed: int = 5
        self.gravity: float = 0.6
        self.jump_speed: float = -14
        self.facing_left: bool = True
        self.on_ground: bool = False
        self.on_ceiling: bool = False
        self.on_left: bool = False
        self.on_right: bool = False

    def get_input(self) -> None:
        keys: List[bool] = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.facing_left = False
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.facing_left = True
        else:
            self.direction.x = 0

        if keys[pygame.K_w] and self.on_ground:
            self.jump()

    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self) -> None:
        self.direction.y = self.jump_speed

    def update(self) -> None:
        self.get_input()

    def save_original_pos(self, pos):
        self.original_pos = pos