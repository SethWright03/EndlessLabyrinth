import pygame

class Player(pygame.sprite.Sprite):
    position = pygame.Vector2(160,480)
    posX = 160
    posY = 480
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.health = 3
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posX,self.posY)
        self.damage_duration = 500
        self.damage_time = 0
    def damage(self):
        self.health -= 1
        self.image.fill('orange')
        self.damage_time = pygame.time.get_ticks()

class Floor_Trap(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.time_step = 0
        self.position = pygame.Vector2(0,0)
        self.activity_state = False
        self.posX = 0
        self.posY = 0
        self.image = pygame.Surface((80,80))
        self.image.fill('black')
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.posX,self.posY)
    def turn(self):
        self.time_step += 1
        if self.time_step == 3:
            self.activity_state = True
            self.image.fill('red')
        if self.time_step == 6:
            self.activity_state = False
            self.image.fill('black')
            self.time_step = 0

class Wall_Tile(pygame.sprite.Sprite):
    position = pygame.Vector2(0,0)
    posX = 0
    posY = 0
    def __init__(self,tilepos_x,tilepos_y):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill('gray')
        self.rect = self.image.get_rect()
        self.rect.topleft = (tilepos_x,tilepos_y)

class Floor_Tile(pygame.sprite.Sprite):
    position = pygame.Vector2(0,0)
    posX = 0
    posY = 0
    def __init__(self,tilepos_x,tilepos_y):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill('white')
        self.rect = self.image.get_rect()
        self.rect.topleft = (tilepos_x,tilepos_y)