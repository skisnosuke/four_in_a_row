import pygame
from piece import Piece
from settings import Settings
class Board:
    # property
    # 列ごとの個数 {1: 0, 2: 0, ...}
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

    def draw_board(self, surface):
        for i in range(self.settings.board_column):
            for j in range(self.settings.board_row):
                pygame.draw.rect(surface, self.settings.board_color, 
                    (self.settings.board_x+i*self.settings.board_grid_width, self.settings.board_y+j*self.settings.board_grid_height,
                    self.settings.board_grid_width, self.settings.board_grid_height), 1)

    # def draw_pieces(self, surface):
    #     for i in range
        

    def select_row(self, x, y):
        self.x = x
        # self.y = y
        if (self.settings.board_x <= self.x and self.x < self.settings.board_x+self.settings.board_grid_width):
            #return 0
            print("0")
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*2):
            #return 1
            print("1")
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*3):
            #return 2
            print("2")
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*4):
            #return 3
            print("3")
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*5):
            #return 4
            print("4")
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*6):
            #return 5
            print("5")
        elif (self.x < self.settings.board_x+self.settings.board_grid_width*7):
            #return 6
            print("6")

    def create_piece(self, x, y, player_num):
        self.pieces.append(Piece(x, y, player_num))

