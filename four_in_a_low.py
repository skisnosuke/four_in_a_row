import sys
import pygame

from settings import Settings
#from boarf import Board
#from piece import Piece

class Four_In_A_Low:
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
        while True:
            #キーボードとマウスのイベントを管理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #画面の再描画
            self.screen.fill(self.settings.bg_color)
            #最新の画面の表示
            pygame.display.flip()

if __name__ == "__main__":
    #ゲームのインスタンスを作成し、実行
    fial = Four_In_A_Low()
    fial.run_game()