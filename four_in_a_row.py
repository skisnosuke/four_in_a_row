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
        self.game_flag = True
        self.ending_flag = False
        self.winner = 0

        pygame.display.set_caption("重力付き四目並べ")

    def run_game(self):
        #ゲームのメインループ
        self.board = Board()
        self.update_screen()

        while True:
            while self.game_flag:
                #キーボードとマウスのイベントを管理
                #どっちかが勝ったらゲーム終了
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
                            self.winner = "winner: player" + str(self.board.pieces[-1].player_num)
                            self.winner_text = self.settings.font2.render(self.winner, True, (255, 255, 0))
                            self.ending_flag = True
                            self.game_flag = False

            self.update_screen()
            while self.ending_flag:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            self.board.reset_board()
            if self.ending_flag:
                self.ending_flag = False
                self.game_flag = True
            self.update_screen()

    def update_screen(self):
        #画面のリセット
        self.screen.fill(self.settings.bg_color)
        #ボードの描画
        self.board.draw_board(self.screen)
        #ピースsの描画
        self.board.draw_pieces(self.screen)
        #テキストの描画
        self.screen.blit(self.settings.text1, (750, 100))
        self.screen.blit(self.settings.text2, (750, 120))

        if self.ending_flag:
            self.screen.blit(self.winner_text, (200, 200))
        #最新の画面の表示
        pygame.display.flip()

if __name__ == "__main__":
    #ゲームのインスタンスを作成し、実行
    fial = FourInARow()
    fial.run_game()