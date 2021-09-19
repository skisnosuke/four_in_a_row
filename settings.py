import pygame
class Settings:
    #設定を格納するクラス
    def __init__(self):
        #初期設定

        """画面設定"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        """駒の設定"""
        self.piece_radius = 32
        self.piece_color_1 = pygame.Color(71, 169, 247)
        self.piece_color_2 = pygame.Color(235, 123, 192)

        """ボードの設定"""
        self.board_x = 150
        self.board_y = 75
        self.board_color = (0, 0, 0)
        self.board_column = 7
        self.board_row = 6
        self.board_grid_width = 80
        self.board_grid_height = 80