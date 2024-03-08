class Menu: 
    def __init__(self, screen):
        self.screen = screen

    
    def pausemenu(self):
        self.screen.fill((0, 255, 0))
    
    def deathmenu(self):
        self.screen.fill((255, 0, 0,))
    
    def menudraw(self, menutype):
        if menutype == "pause":
            self.pausemenu()
        elif menutype == "death":
            self.deathmenu()