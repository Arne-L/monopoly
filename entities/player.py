from entities.tile import Tile
from core.board import Board

class Player:
    def __init__(self, name: str, balance: int, id: int):
        self.name: str = name
        self.balance: int = balance
        self.position: int = 0
        self.id: int = id

    def get_current_tile(self, board: Board) -> Tile:
        return board.get_tile_at(self.position)
    
    def get_score(self, board: Board) -> int:
        return self.balance + sum([owned_tile.get_current_value() for owned_tile in board.get_tiles_of(self.id)])