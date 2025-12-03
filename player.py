import pygame
from utils import SCREEN_WIDTH, SCREEN_HEIGHT, GREEN

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        import os
        self.image = pygame.image.load(os.path.join('Sprites', 'Player.png')).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 40))
        
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed_x = 0
        self.speed = 8

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -self.speed
        if keystate[pygame.K_RIGHT]:
            self.speed_x = self.speed
            
        self.rect.x += self.speed_x
        
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        from bullet import Bullet
        return Bullet(self.rect.centerx, self.rect.top)
