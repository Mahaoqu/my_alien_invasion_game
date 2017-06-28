class Settings():
    def __init__(self):
        """初始化游戏的静态设置"""
        #设置屏幕
        self.screen_width = 1366
        self.screen_height = 700
        self.bg_color = (230,230,230)
        #设置飞船
        self.ship_limit = 3
        #设置子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 5
        #设置外星人
        self.fleet_drop_speed = 10
        #加快游戏节奏的速度
        self.speedup_scale = 1.1
        # 记分
        # TODO：Accomplish it！

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化动态设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.fleet_direction = 1 # 1代表向右，-1代表向左

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale