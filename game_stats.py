# coding:gbk
import json


class GameStats(object):
    """������Ϸ��ͳ����Ϣ"""

    def __init__(self, ai_settings):
        """��ʼ��ͳ����Ϣ"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # ����Ϸһֱ���ڷǻ״̬
        self.game_active = False

        # ���κ�����¶���Ӧ������ߵ÷�
        filename = 'high_score.json'
        try:
            with open(filename) as f_obj:
                self.high_score = json.load(f_obj)
        except FileNotFoundError:
            self.high_score = 0

    def reset_stats(self):
        """��ʼ������Ϸ�����ڼ���ܱ仯��ͳ����Ϣ"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
