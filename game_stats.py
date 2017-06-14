class GameStats():
    """游戏的统计信息"""

    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_sittings = ai_settings
        self.reset_stats()
        self.game_active = True #游戏的运行状态

    def reset_stats(self):

        self.ships_left = self.ai_sittings.ship_limit