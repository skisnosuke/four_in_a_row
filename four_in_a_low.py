from pygame.locals import *
import sys
import pygame

from settings import Settings
from board import Board
from piece import Piece

class FourInALow:
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
        
        while True:
            #キーボードとマウスのイベントを管理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    x, y = event.pos
                    self._select_row(x, y)

            self._update_screen()

    def _update_screen(self):
        #画面の再描画
        self.screen.fill(self.settings.bg_color)
        #ボードの描画
        self.board.draw(self.screen)
        #最新の画面の表示
        pygame.display.flip()

    def _select_row(self, x, y):
        #x,y座標からから列を選択 pieceに持たせた方がいいかも
        self.x = x
        # self.y = y
        if (150 <= self.x and self.x < 250):
            #return 0
            print("0")
        elif (self.x < 350):
            #return 1
            print("1")
        elif (self.x < 450):
            #return 2
            print("2")
        elif (self.x < 550):
            #return 3
            print("3")
        elif (self.x < 650):
            #return 4
            print("4")
        elif (self.x < 750):
            #return 5
            print("5")
        elif (self.x < 850):
            #return 6
            print("6")



if __name__ == "__main__":
    #ゲームのインスタンスを作成し、実行
    fial = FourInALow()
    fial.run_game()