import pygame
from tiles import *
from settings import *
from player import Gepesz
from infos import Infos
from enemy import Cigany
from menu import Menu
from events import *
from timer import *


class Level:
    button_pos_offset = 23
    BUTTON_SPEED = 3
    button_original_pos: int = 0
    button_onoff_infos: bool = False
    button_onoff_gepesz: bool = False
    full_lift: list[Lift] = []
    lift_original: tuple = 0, 0
    switch_on: bool = False
    infos_alive: bool = True
    gepesz_alive: bool = True
    switch_pic: str = "graphics/temp/switch_off.png"
    lift_max: int = 0
    current_level: list[str] = level_choice
    background_image: int = "graphics/map/palyavalasztos(folyoso).png"
    infos_finished: bool = False
    gepesz_finished: bool = False

    def __init__(self, surface, infos, gepesz, cigany, font, clock, score):
        self.display_surface = surface
        self.tiles_dict = {}
        self.players = pygame.sprite.Group()
        self.infos = infos
        self.gepesz = gepesz
        self.enemies = pygame.sprite.Group()
        self.cigany = cigany
        self.menu_object = Menu(surface)
        self.setup_level(self.current_level)
        self.game_font = font
        self.timer = clock
        self.scorecounter = score

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for coll_index, cell in enumerate(row):
                if cell == "S":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile_X = Tile((x, y))
                    self.tiles.add(tile_X)
                elif cell == "I":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.infos.rect.topleft = (x, y)
                    self.players.add(self.infos)
                    self.infos.save_original_pos((x, y))
                elif cell == "G":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.gepesz.rect.topleft = (x, y)
                    self.players.add(self.gepesz)
                    self.gepesz.save_original_pos((x, y))
                elif cell == "E":
                    x = coll_index * tile_size
                    y = row_index * tile_size - 33
                    self.cigany.rect.topleft = (x, y)
                    self.enemies.add(self.cigany)
                    self.cigany.save_original_pos((x, y))
                elif cell == "W":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    tile_X = Water((x, y))
                    self.tiles.add(tile_X)
                elif cell == "L":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.lift = Lift((x, y))
                    self.tiles.add(self.lift)
                    self.full_lift.append(self.lift)
                    self.lift_original = self.lift.rect.y
                elif cell == "B":
                    x = coll_index * tile_size
                    y = row_index * tile_size + self.button_pos_offset
                    self.button = Button((x, y))
                    self.tiles.add(self.button)
                    self.button_original_pos = self.button.rect.y
                elif cell == "K":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.switch = Switch((x, y), self.switch_pic)
                    self.tiles.add(self.switch)
                elif cell == "A":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.barrier = Barrier((x, y))
                    self.tiles.add(self.barrier)
                elif cell == "D":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.barrier = Asztal((x, y))
                    self.tiles.add(self.barrier)
                elif cell == "C":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.actiave = Activate((x, y))
                    self.tiles.add(self.actiave)
                elif cell == "T":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.csempe = Csempe((x, y))
                    self.tiles.add(self.csempe)
                elif cell == "P":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.parketta = Parketta((x, y))
                    self.tiles.add(self.parketta)
                elif cell == "s":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.szek = Szék((x, y))
                    self.tiles.add(self.szek)
                elif cell == "i":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.szek = Finished_check((x, y))
                    self.tiles.add(self.szek)
                elif cell == "F":
                    x = coll_index * tile_size
                    y = row_index * tile_size - 15
                    self.szek = Ajtó((x, y))
                    self.tiles.add(self.szek)
                elif cell == "H":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.platform = Platform((x, y))
                    self.tiles.add(self.platform)

    def level_reset(self):
        for player in self.players:
            player.rect.topleft = (player.original_pos)
        for enemy in self.enemies:
            enemy.rect.topleft = (enemy.original_pos)
        self.switch_on = False
        self.switch_pic = "graphics/temp/switch_off.png"

    def lift_up(self):
        for i in self.full_lift:
            if i.rect.y > self.lift_max:
                i.rect.y -= 4

    def lift_down(self):
        for i in self.full_lift:
            if self.lift_original > i.rect.y:
                i.rect.y += 1.5

    def run(self):
        self.players.update()
        self.players.draw(self.display_surface)
        self.enemies.draw(self.display_surface)
        self.horizontal_collision()
        self.vertical_collision()
        self.tiles.draw(self.display_surface)
        self.enemy_movement()
        self.map_choose()
        self.timer.time_print()
        if self.current_level == level_choice:
            self.lift_max = 450
            self.background_image = "graphics/map/palyavalasztos(folyoso).png"
        elif self.current_level == level_map_1:
            self.lift_max = 650
            self.background_image = "graphics/map/jedlik_epulet.png"
        elif self.current_level == level_map_7:
            self.lift_max = 610
            self.background_image = "graphics/map/jedlik_epulet.png"

        if not self.infos_alive or not self.gepesz_alive:
            pygame.event.post(pygame.event.Event(event_death))
        self.menu_object.delete_all()

        if self.infos_finished and self.gepesz_finished:
            pygame.event.post(pygame.event.Event(event_win))

    def pausemenu(self):
        self.menu_object.menudraw("pause")
        self.scorecounter.score_print()

    def deathmenu(self):
        self.menu_object.menudraw("death")
        self.timer.reset_timer()
        self.scorecounter.score_print()

    def winscreen(self):
        self.menu_object.menudraw("win")
        self.scorecounter.win()
        self.timer.reset_timer()
        self.scorecounter.score_print()

    def screen_fill(self, screen, BACKGROUND):
        screen.blit(BACKGROUND, (0, 0))

    def unlockmap():
        pass

    def enemy_movement(self):
        for enemy in self.enemies:
            if enemy.facing_left:
                enemy.rect.x -= enemy.speed
            else:
                enemy.rect.x += enemy.speed
            for sprite in self.tiles.sprites():
                if isinstance(sprite, Barrier):
                    if sprite.rect.colliderect(enemy.rect):
                        if enemy.facing_left:
                            enemy.facing_left = False
                        else:
                            enemy.facing_left = True
                if isinstance(sprite, Tile):
                    if sprite.rect.colliderect(enemy.rect):
                        if enemy.facing_left:
                            enemy.facing_left = False
                        else:
                            enemy.facing_left = True

    def horizontal_collision(self):
        for player in self.players:
            player.rect.x += player.direction.x * player.speed

            for sprite in self.tiles.sprites():
                if isinstance(sprite, Water):
                    continue
                if isinstance(sprite, Barrier):
                    continue
                if isinstance(sprite, Ajtó):
                    continue
                if isinstance(sprite, Switch):
                    if sprite.rect.colliderect(player.rect):
                        if player.direction.x > 0 and player.rect.left < sprite.rect.left:
                            self.switch_on = True
                        elif player.direction.x < 0 and player.rect.right > sprite.rect.right:
                            self.switch_on = False
                            self.switch_pic = "graphics/temp/switch_off.png"
                        else:
                            self.switch_on = False
                    sprite.update_image(self.switch_on)
                for other_player in self.players:
                    if other_player != player and player.rect.colliderect(other_player.rect):
                        if player.direction.x > 0:
                            player.rect.right = other_player.rect.left
                        elif player.direction.x < 0:
                            player.rect.left = other_player.rect.right
                for enemy in self.enemies:
                    if enemy.rect.colliderect(player.rect):
                        if player == self.infos:
                            self.infos_alive = False
                        elif player == self.gepesz:
                            self.gepesz_alive = False

                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left

    def map_choose(self) -> None:
        for player in self.players:
            if self.current_level == level_choice:
                keys: List[bool] = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and 108 < player.rect.x < 250 and 800 < player.rect.y < 900 and maplock.get("level_map_1") == "unlocked":
                    self.setup_level(level_map_1)
                    self.current_level = level_map_1
                    self.background_image = "graphics/map/terem_hatter.png"
                elif keys[pygame.K_SPACE] and 540 < player.rect.x < 680 and 680 < player.rect.y < 900 and maplock.get("level_map_2") == "unlocked":
                    self.setup_level(level_map_2)
                    self.current_level = level_map_2
                elif keys[pygame.K_SPACE] and 990 < player.rect.x < 1130 and 680 < player.rect.y < 900 and maplock.get("level_map_3") == "unlocked":
                    self.setup_level(level_map_3)
                    self.current_level = level_map_3
                elif keys[pygame.K_SPACE] and 1410 < player.rect.x < 1540 and 680 < player.rect.y < 900 and maplock.get("level_map_4") == "unlocked":
                    self.setup_level(level_map_4)
                    self.current_level = level_map_4
                elif keys[pygame.K_SPACE] and 1580 < player.rect.x < 1730 and 220 < player.rect.y < 480 and maplock.get("level_map_5") == "unlocked":
                    self.setup_level(level_map_5)
                    self.current_level = level_map_5
                elif keys[pygame.K_SPACE] and 1190 < player.rect.x < 1340 and 220 < player.rect.y < 480 and maplock.get("level_map_6") == "unlocked":
                    self.setup_level(level_map_6)
                    self.current_level = level_map_6
                elif keys[pygame.K_SPACE] and 800 < player.rect.x < 940 and 220 < player.rect.y < 480 and maplock.get("level_map_7") == "unlocked":
                    self.setup_level(level_map_7)
                    self.current_level = level_map_7
                elif keys[pygame.K_SPACE] and 430 < player.rect.x < 570 and 220 < player.rect.y < 480 and maplock.get("level_map_8") == "unlocked":
                    self.setup_level(level_map_8)
                    self.current_level = level_map_8
                elif keys[pygame.K_SPACE] and 90 < player.rect.x < 230 and 220 < player.rect.y < 480 and maplock.get("level_map_9") == "unlocked":
                    self.setup_level(level_map_9)
                    self.current_level = level_map_9

    def vertical_collision(self):

        for player in self.players:
            player.apply_gravity()

            for sprite in self.tiles.sprites():
                if isinstance(sprite, Barrier):
                    continue
                if isinstance(sprite, Water):
                    continue
                if isinstance(sprite, Ajtó):
                    continue
                if isinstance(sprite, Finished_check):
                    if sprite.rect.colliderect(self.infos.rect):
                        self.infos_finished = True
                    if sprite.rect.colliderect(self.gepesz.rect):
                        self.gepesz_finished = True

                if isinstance(sprite, Button):
                    if sprite.rect.colliderect(player.rect):
                        if player == self.infos:
                            self.button_onoff_infos = True
                        if player == self.gepesz:
                            self.button_onoff_gepesz = True
                    else:
                        if player == self.infos:
                            self.button_onoff_infos = False
                        if player == self.gepesz:
                            self.button_onoff_gepesz = False

                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        player.on_ground = True
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                        player.on_ceiling = True
            for other_player in self.players:
                if other_player != player and player.rect.colliderect(other_player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = other_player.rect.top
                        player.direction.y = 0
                        player.on_ground = True
                    elif player.direction.y < 0:
                        player.rect.top = other_player.rect.bottom
                        player.direction.y = 0
                        player.on_ceiling = True
            for enemy in self.enemies:
                if enemy.rect.colliderect(player.rect):
                    enemy.kill()

        for player in self.players:
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False

        if self.button_onoff_infos or self.button_onoff_gepesz:
            if self.button_onoff_infos or self.button_onoff_gepesz:
                self.button.rect.y += 1.5
            self.lift_up()
        elif self.switch_on:
            self.lift_up()
            if self.button_original_pos <= self.button.rect.y:
                self.button.rect.y -= 1
        else:
            if self.button_original_pos <= self.button.rect.y:
                self.button.rect.y -= 1
            else:
                self.lift_down()
