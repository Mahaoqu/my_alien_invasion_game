import pygame.font

class ScoreBoard():
    """显示得分信息"""
    
    def __init__(self, ai_settings, screen, stats):
        """初始化得分属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #设置字体信息
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #准备初始得分图像
        self.prep_score()
    
    def prep_score(self):
        """将得分渲染成图像"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
            self.text_color, self.ai_settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score():
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)