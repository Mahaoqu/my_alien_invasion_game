import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
def start_game(ai_settings, screen, stats, ship, aliens, bullets):
    """重置并开始新的游戏"""
    pygame.mouse.set_visible(False) #隐藏光标
    stats.reset_stats()
    stats.game_active = True 
    ai_settings.increase_speed() #重置游戏统计信息
    
    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

def check_keydown_events(event,ai_settings, screen, stats, ship, aliens, bullets):
    """响应按下"""
    #响应左右移动
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT: #一个事件仅与一个键相关联
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_p and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)

def check_keyup_events(event,ai_settings, screen, ship, bullets):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False   
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """响应键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings, screen, stats, ship, aliens, bullets) 
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ai_settings, screen, ship, bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
        bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens,
        bullets, mouse_x, mouse_y):
    """点击开始按钮时，开始新游戏"""
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        start_game(ai_settings, screen, stats, ship, aliens, bullets)

def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button):
    """更新屏幕上的图像，并切换到新屏幕""" 
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    
    if not stats.game_active:
        play_button.draw_button() #如果游戏未开始则绘制开始按钮

    pygame.display.flip() #显示新屏幕


def update_bullets(ai_settings, screen, ship, aliens ,bullets):
    """更新子弹的位置，删除已消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens ,bullets)
    
def fire_bullet(ai_settings, screen, ship, bullets):
    """控制发射子弹"""
    if len(bullets) < ai_settings.bullets_allowed:
         new_bullet = Bullet(ai_settings, screen, ship)
         bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """计算每行能容纳的外星人数目"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人，并放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number 
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳外星人的行数"""
    available_space_y = (ai_settings.screen_height - 
                          (3* alien_height) - ship_height )
    number_rows = int(available_space_y / ( 2 * alien_height ))
    return number_rows

def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    alien = Alien(ai_settings,screen) #获取一个外星人的属性
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, 
                row_number)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被撞到的飞船"""
    if stats.ships_left >0 :
        stats.ships_left -= 1 #剩余飞船数目减一

        aliens.empty()
        bullets.empty() #清空子弹和外星人

        create_fleet(ai_settings, screen, ship, aliens) #创建新的外星人组
        ship.center_ship() #新建一艘飞船

        sleep(0.5) #延时0.5s
    
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """更新外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update() #对Sprite中对象自动为每一个对象调用update

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
        

def check_fleet_edges(ai_settings, aliens):
    """检查外星人到达屏幕边缘时"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break

def change_fleet_direction(ai_settings,aliens):
    """改变外星人队列的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens ,bullets):
    """判断子弹是否与外星人发生了碰撞，如果是则使其消失"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0: #如果没有外星人，则新建一群外星人，并增加一级难度
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets) #像飞船被撞到一样处理
            break