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
        self.x = (self.settings.board_x + self.settings.board_grid_width * self.column
                + self.settings.board_grid_width * 0.5)
        self.y = (self.settings.board_y + self.settings.board_row * self.settings.board_grid_height - 
            (self.settings.board_grid_height * self.row + self.settings.board_grid_height * 0.5))
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.settings.piece_radius)

    def drop(self, surface, board):
        self.x = self.settings.board_x + self.settings.board_grid_width * self.column + self.settings.board_grid_width * 0.5
        self.y = self.settings.board_y + self.settings.board_grid_height / 2
        while(self.y < self.settings.board_y + self.settings.board_row * self.settings.board_grid_height - (self.settings.board_grid_height * self.row + self.settings.board_grid_height * 0.5)):
            surface.fill(self.settings.bg_color)
            board.draw_board(surface)
            for piece in board.pieces[0:-1]:
                piece.draw(surface)
            pygame.draw.circle(surface, self.color, (self.x, self.y), self.settings.piece_radius)
            pygame.display.update()
            pygame.time.wait(1)
            self.y += 2
        self.draw(surface)
        pygame.display.flip()