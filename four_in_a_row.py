from pygame.locals import *
import sys
import pygame
from settings import Settings
from board import Board

class FourInARow:
    #ゲームのアセットと動作を管理する全体的なクラス
    def __init__(self):
        #ゲームを初期化し、ゲームのリソースを作成する
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("重力付き四目並べ")

    def run_game(self):
        #ゲームのメインループ
        self.board = Board()
        self.update_screen()
        
        while True:
            #キーボードとマウスのイベントを管理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self.board.create_piece(x)
                    self.board.pieces[-1].drop(self.screen, self.board)
                    self.update_screen()
                    if self.board.is_win():
                        print("winner:", self.board.pieces[-1].player_num)

               


    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            self.board.reset_board()
            self.update_screen()

    def update_screen(self):
        #画面のリセット
        self.screen.fill(self.settings.bg_color)
        #ボードの描画
        self.board.draw_board(self.screen)
        #ピースsの描画
        self.board.draw_pieces(self.screen)
        #最新の画面の表示
        pygame.display.flip()

if __name__ == "__main__":
    #ゲームのインスタンスを作成し、実行
    fial = FourInARow()
    fial.run_game()