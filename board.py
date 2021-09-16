from settings import Settings
class Board:
    # property
    # self.height
    # self.width
    # 列ごとの高さ {1: 0, 2: 0, ...}
    # pieces : [piece, piece, ..]

    # method
    # 置く
        # 下から見てって 空なら置く 6を超えたら 置き直させる
    # 勝利判定
        # 縦横斜め
    # 列の高さの更新


    def __init__(self):
        self.settings = Settings()
        self.pieces = []

