from entities.tile import Tile
from core.board import Board

class Player:
    def __init__(self, name: str, balance: int):
        self.name = name
        self.balance = balance
        self.position = 0

    def get_current_tile(self, board: Board) -> Tile:
        return board.get_tile_at(self.position)