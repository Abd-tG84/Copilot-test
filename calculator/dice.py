import random

class Dice:
    def __init__(self, sides=6):
        """
        sides: サイコロの面の数（デフォルトは6面）
        """
        if sides < 1:
            raise ValueError("サイコロの面の数は1以上でなければなりません")
        self.sides = sides

    def roll(self):
        """
        サイコロを振り、1から面の数までのランダムな値を返す
        """
        return random.randint(1, self.sides)