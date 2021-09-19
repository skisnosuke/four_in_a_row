import pygame
from settings import Settings
class Board:
    # property
    # self.height
    # self.width
    # 列ごとの高さ {1: 0, 2: 0, ...}
    # pieces : [piece, piece, ..]

    # method
    # 描画
    # 置く
        # 下から見てって 空なら置く 6を超えたら 置き直させる
    # 勝利判定
        # 縦横斜め
    # 列の高さの更新


    def __init__(self):
        self.settings = Settings()
        self.pieces = []

    def draw(self, surface):
        i = 0
        while i < self.settings.board_column:
            j=0
            while j < self.settings.board_row:
                pygame.draw.rect(surface, self.settings.board_color, 
                    (self.settings.board_x+i*75, self.settings.board_y+j*75, 
                    self.settings.board_grid_width, self.settings.board_grid_height), 1)
                j+=1
            i+=1
