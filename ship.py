import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_setings, screen):
        super(Ship, self).__init__()
        self.screen = screen

        # загрузка изображения корабля и получения прямоугольника
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.ai_setings = ai_setings

        # задал координаты для корабля

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_setings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        # рисуем корабль при помощи метода blit
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx
