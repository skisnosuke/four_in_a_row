import pygame
class Settings:
    #設定を格納するクラス
    def __init__(self):
        #初期設定

        """画面設定"""
        self.screen_width = 1000
        self.screen_height =600
        self.bg_color = (230, 230, 230)

        """駒の設定"""
        self.piece_width = 1
        self.piece_height = 1
        self.piece_color_1 = pygame.Color.r
        self.piece_color_2 = pygame.Color.b

        """ボードの設定"""
        self.board_width = 7 
        self.board_height = 6

        """ボードの矩形の設定"""
        self.board_x = 150
        self.board_y = 75
        self.board_rect_x = 100
        self.board_rect_y = 75
        self.board_color = (0, 0, 0)