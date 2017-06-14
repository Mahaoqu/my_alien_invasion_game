import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """玩家射出的子弹"""

    def __init__(self,ai_settings,screen,ship):
        """创建子弹对象"""
        super().__init__()
        self.screen = screen
        #初始化子弹的位置，创建一个矩形对象表示
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,
                ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #存储子弹的位置
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """更新子弹的位置，向上移动"""
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen,self.color,self.rect)