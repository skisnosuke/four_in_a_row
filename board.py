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

    def draw(self, screen):
        i = 0
        while i < self.settings.board_width:
            j=0
            while j < self.settings.board_height:
                pygame.draw.rect(screen, self.settings.board_color, 
                    (self.settings.board_x+i*100, self.settings.board_y+j*75, 
                    self.settings.board_rect_x, self.settings.board_rect_y), 1)
                j+=1
            i+=1
