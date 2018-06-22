# coding:gbk
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard(object):
    """��ʾ�÷���Ϣ����"""

    def __init__(self, ai_settings, screen, stats):
        """��ʼ����ʾ�÷��漰������"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # ��ʾ�÷���Ϣʱʹ�õ���������
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("Times New Roman", 32)
        self.prep_images()

    def prep_images(self):
        """׼�������÷ֺͷɴ������ĳ�ʼͼ��"""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """���÷�ת��Ϊ��Ⱦ��ͼ��"""
        rounded_score = int(round(self.stats.score, -1))  # -1��ʾԲ����10��
        score_str = "{:,}".format(rounded_score)  # �����ּ���붺�ţ� ��1,000,000
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # ���÷ַ�����Ļ���Ͻ�
        self.score_rect = self.score_image.get_rect()
        self.score_rect.left = self.screen_rect.left + 10
        self.score_rect.top = 10

    def prep_high_score(self):
        """����ߵ÷�ת��Ϊ��Ⱦ��ͼ��"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = ("High Score: " + "{:,}").format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        # ����ߵ÷ַ�����Ļ��������
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """���ȼ�ת��Ϊ��Ⱦ��ͼ��"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)

        # ���ȼ����ڵ÷��·�
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.score_rect.left
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """��ʾ�����¶����ҷɴ�"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.right = (self.screen_rect.right - 10 -
                               ship_number * ship.rect.width)
            ship.rect.top = 10
            self.ships.add(ship)

    def show_score(self):
        """����Ļ����ʾ��ǰ�÷ֺ���ߵ÷�"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
