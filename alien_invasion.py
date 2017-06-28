#!/usr/bin/python3
import pygame
from ship import Ship
from alien import Alien
from settings import Settings
from game_stats import GameStats
from button import Button
import game_function as gf
from scoreboard import ScoreBoard
from pygame.sprite import Group



def run_game(): 
    pygame.init()

    ai_settings = Settings()
    stats = GameStats(ai_settings) 
    sb = ScoreBoard(ai_settings, screen, stats) #初始化设置和统计信息

    screen = pygame.display.set_mode(
            (ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion") #初始化屏幕和窗口
    
    play_button = Button(ai_settings, screen,"Play!") #初始化开始按钮
    
    #初始化飞船、子弹组和外星人组
    ship = Ship(ai_settings,screen)
    bullets = Group()
    aliens = Group()
    
    gf.create_fleet(ai_settings, screen, ship, aliens)
    #游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active == True:
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens ,bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()