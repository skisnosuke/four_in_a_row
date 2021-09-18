import pygame
from settings import Settings
class Piece:
    # property
    # self.x
    # self.y
    # どっちサイドか player_num 1 or 2

    # method

    def __init__(self, x, y, player_num):
        self.settings = Settings()
        self.x = x
        self.y = y
        self.player_num = player_num
        self.color = player_num == 1 if self.settings.piece_color_1 else self.settings.piece_color_2
        self.rect = pygame.Rect(0, 0, 10, 10)