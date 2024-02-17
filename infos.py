from typing import List
import pygame

class Infos(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int]) -> None:
        super().__init__()

        self.image = pygame.image.load("graphics/temp/test_character.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.frame_index: float = 0
        self.direction = pygame.math.Vector2(0, 0)
        self.speed: int = 8
        self.gravity: float = 0.6
        self.jump_speed: float = -16
        self.facing_left: bool = True
        self.on_ground: bool = False
        self.on_ceiling: bool = False
        self.on_left: bool = False
        self.on_right: bool = False

    def get_input(self) -> None:
        keys: List[bool] = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_left = False
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_left = True
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.on_ground:
            self.jump()

    def apply_gravity(self) -> None:
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self) -> None:
        self.direction.y = self.jump_speed

    def update(self) -> None:
        self.get_input()