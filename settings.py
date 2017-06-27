class Settings():
    def __init__(self):
        #设置屏幕
        self.screen_width = 1366
        self.screen_height = 700
        self.bg_color = (230,230,230)
        #设置飞船
        self.ship_speed_factor = 2.5
        self.ship_limit = 3
        #设置子弹
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5
        #设置外星人
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 50
        self.fleet_direction = 1 # 1代表向右，-1代表向左