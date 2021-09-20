import pygame
from piece import Piece
from settings import Settings
class Board:
    # property
        # 列ごとの個数 count_each_column {1: 0, 2: 0, ...}
        # pieces : [piece, piece, ..]
        # player_num 1 or 2

    # method
        # 描画
        # 置く
            # 下から見てって 空なら置く 6を超えたら 置き直させる
            # 列の個数の更新
        # 勝利判定
            # 縦横斜め

    def __init__(self):
        self.settings = Settings()
        self.pieces = []
        self.count_each_column = {i: 0 for i in range(self.settings.board_column)}
        self.player_num = 1

    def draw_board(self, surface):
        for i in range(self.settings.board_column):
            for j in range(self.settings.board_row):
                pygame.draw.rect(surface, self.settings.board_color, 
                    (self.settings.board_x+i*self.settings.board_grid_width, self.settings.board_y+j*self.settings.board_grid_height,
                    self.settings.board_grid_width, self.settings.board_grid_height), 1)

    def draw_pieces(self, surface):
        for piece in self.pieces:
            piece.draw(surface)
        
    def get_column(self, x):
        self.x = x
        if (self.settings.board_x <= self.x and self.x < self.settings.board_x+self.settings.board_grid_width):
            return 0
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*2):
            return 1
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*3):
            return 2
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*4):
            return 3
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*5):
            return 4
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*6):
            return 5
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*7):
            return 6

    def create_piece(self, x):
        self.column = self.get_column(x)
        self.row = self.count_each_column[self.column]
        if self.row < self.settings.board_row:
            self.count_each_column[self.column] += 1
            self.pieces.append(Piece(self.column, self.row, self.player_num))
            self.player_num = 2 if self.player_num == 1 else 1

    # def is_end(self):
    #     for piece in self.pieces:
            # piece.