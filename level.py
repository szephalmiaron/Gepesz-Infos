import pygame
from tiles import Tile, Water, Lift, Button, Switch, Barrier, Activate
from settings import tile_size, level_map_1, level_choice
from player import Gepesz
from infos import Infos
from enemy import Cigany
from menu import Menu

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
    background_image = "graphics/map/palyavalasztos(folyoso).png"
    def __init__(self, surface, infos, gepesz, cigany):
        self.display_surface = surface
        self.tiles_dict = {}
        self.players = pygame.sprite.Group()  
        self.infos = infos  
        self.gepesz = gepesz  
        self.enemies = pygame.sprite.Group()
        self.cigany = cigany
        self.menu_object = Menu(surface)


        self.setup_level(self.current_level)


    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        row_index = 0




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
                elif cell == "G":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.gepesz.rect.topleft = (x, y)  
                    self.players.add(self.gepesz)
                elif cell == "E":
                    x = coll_index * tile_size
                    y = row_index * tile_size - 33
                    self.cigany.rect.topleft = (x, y)
                    self.enemies.add(self.cigany)  
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
                elif cell == "C":
                    x = coll_index * tile_size
                    y = row_index * tile_size
                    self.barrier = Activate((x, y))
                    self.tiles.add(self.barrier)

    def lift_up(self):
        for i in self.full_lift:
            if i.rect.y > self.lift_max:
                i.rect.y -= 4

    def lift_down(self):
        for i in self.full_lift:
            if self.lift_original > i.rect.y:
                i.rect.y += 1.5

    



    def run(self, paused, alive):
        if paused:
            self.menu_object.menudraw("pause")
        elif not alive:
            self.menu_object.menudraw("death")
        else:
            self.players.update()
            self.players.draw(self.display_surface)
            self.enemies.draw(self.display_surface)
            self.horizontal_collision()
            self.vertical_collision()
            self.tiles.draw(self.display_surface)
            self.enemy_movement()
            if self.current_level == level_choice:
                self.lift_max = 450
                self.background_image = "graphics/map/palyavalasztos(folyoso).png"
            elif self.current_level == level_map_1:
                self.lift_max = 650
                self.background_image = "graphics/map/jedlik_epulet.png"
            if self.infos_alive and self.gepesz_alive:
                return True
            else:
                return False
        
    def menu(self, surface):
        surface.fill((111, 152, 87))

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
                if isinstance(sprite,Tile):
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
                if isinstance(sprite, Activate):
                    if sprite.rect.colliderect(player.rect):
                        self.current_level = level_map_1
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

    def vertical_collision(self):
        for player in self.players:
            player.apply_gravity()

            for sprite in self.tiles.sprites():
                if isinstance(sprite, Barrier):
                    continue
                if isinstance(sprite, Water):
                    continue
                if isinstance(sprite, Activate):
                    if sprite.rect.colliderect(player.rect):
                        self.current_level = level_map_1
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

        if self.button_onoff_infos is True or self.button_onoff_gepesz is True:
            if self.button_onoff_infos is True or self.button_onoff_gepesz is True:
                self.button.rect.y += 1.5
            self.lift_up()
        elif self.switch_on is True:
            self.lift_up()
            if self.button_original_pos <= self.button.rect.y:
                self.button.rect.y -= 1
        else:
            if self.button_original_pos <= self.button.rect.y:
                self.button.rect.y -= 1
            else:
                self.lift_down()
