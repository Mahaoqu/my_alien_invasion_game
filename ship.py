import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """玩家控制的飞船"""
    def __init__(self,ai_settings,screen):
        super(Ship,self).__init__()
        
        self.screen = screen
        self.ai_settings = ai_settings
        
        #加载飞船图片，生成矩形对象
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #新飞船位置在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)

        #移动标志，触发标志时即左右移动
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """更新自己的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

        
    def blitme(self):
        """在屏幕上显示飞船"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """让飞船在屏幕居中"""
        self.center = self.screen_rect.centerx