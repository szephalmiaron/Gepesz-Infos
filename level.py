import pygame
from tiles import Tile, Water, Lift, Button, Switch
from settings import tile_size
from player import Gepesz
from infos import Infos

class Level:
    button_pos_offset = 23
    BUTTON_SPEED = 3
    button_original_pos: int = 0
    button_onoff_infos: bool = False
    button_onoff_gepesz: bool = False
    full_lift: list[Lift] = []
    lift_original: tuple = 0, 0
    switch_on: bool = False
    switch_pic: str = "graphics/temp/switch_off.png"
    def __init__(self, level_data, surface, infos, gepesz):
        self.display_surface = surface
        self.tiles_dict = {}
        self.players = pygame.sprite.Group()  
        self.infos = infos  
        self.gepesz = gepesz  



        self.setup_level(level_data)


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

    def lift_up(self):
        for i in self.full_lift:
            if i.rect.y > 650:
                i.rect.y -= 4

    def lift_down(self):
        for i in self.full_lift:
            if self.lift_original > i.rect.y:
                i.rect.y += 1.5

    

    def run(self):
        self.players.update()
        self.players.draw(self.display_surface)
        self.horizontal_collision()
        self.vertical_collision()
        self.tiles.draw(self.display_surface)    
        print(self.switch_on)

    def horizontal_collision(self):
        for player in self.players:
            player.rect.x += player.direction.x * player.speed

            for sprite in self.tiles.sprites():
                if isinstance(sprite, Water):
                    continue
                if isinstance(sprite, Button):
                    pass
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

                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left

    def vertical_collision(self):
        for player in self.players:
            player.apply_gravity()

            for sprite in self.tiles.sprites():
                if isinstance(sprite, Water):
                    continue

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
        
        for player in self.players:
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False

        if self.button_onoff_infos == True or self.button_onoff_gepesz == True or self.switch_on == True:
            if self.button_onoff_infos == True or self.button_onoff_gepesz == True:
                self.button.rect.y += 1.5
            self.lift_up()
        else:
            if self.button_original_pos <= self.button.rect.y:
                self.button.rect.y -= 1
            else:
                self.lift_down()
