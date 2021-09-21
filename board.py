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
        
    def _get_column(self, x):
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
        self.column = self._get_column(x)
        self.row = self.count_each_column[self.column]
        if self.row < self.settings.board_row:
            self.count_each_column[self.column] += 1
            self.pieces.append(Piece(self.column, self.row, self.player_num))
            self.player_num = 2 if self.player_num == 1 else 1

    def is_win(self):
        last_piece = self.pieces[-1]
        self.verticals = []
        self.horizontals = []
        self.obliques_pos = []
        self.obliques_neg = []
        for piece in self.pieces:
            if piece.player_num == last_piece.player_num:
                if piece.column == last_piece.column:
                    self.verticals.append(piece.row)
                if piece.row == last_piece.row:
                    self.horizontals.append(piece.column)
                if piece.column - piece.row == last_piece.column - last_piece.row:
                    self.obliques_pos.apppend(piece.row)
                if piece.column + piece.row == last_piece.column + last_piece.row:
                    self.obliques_neg.append(piece.row)
        return self._is_continuous_four(self.verticals) | self._is_continuous_four(self.horizontals) | self._is_continuous_four(self.obliques_pos) | self._is_continuous_four(self.obliques_neg)
    
    def _is_continuous_four(self, nums):
        nums.sort()
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] - nums[i+1] == 1:
                count += 1
            else:
                count = 0
        if count == 3:
            return True
        else:
            return False
