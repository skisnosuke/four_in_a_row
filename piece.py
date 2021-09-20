import pygame
from settings import Settings
class Piece:
    def __init__(self, c, r, player_num):
        self.settings = Settings()
        self.column = c
        self.row = r
        self.player_num = player_num
        self.color =  self.settings.piece_color_1 if player_num == 1 else self.settings.piece_color_2

    def draw(self, surface):
        self.x = self.settings.board_x + self.settings.board_grid_width * self.column + self.settings.board_grid_width * 0.5
        self.y = self.settings.board_y + self.settings.board_row * self.settings.board_grid_height - (self.settings.board_grid_height * self.row + self.settings.board_grid_height * 0.5)
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.settings.piece_radius)