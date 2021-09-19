import pygame
from settings import Settings
class Piece:
    def __init__(self, x, y, player_num):
        self.settings = Settings()
        self.x = x
        self.y = y
        self.player_num = player_num
        self.color =  self.settings.piece_color_1 if player_num == 1 else self.settings.piece_color_2

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.settings.piece_radius)