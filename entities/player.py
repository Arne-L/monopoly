from entities.tile import Tile
from entities.cards import Card
from entities.die import Die
from core.board import Board
from typing import Callable
from settings import PRISON_TILE


class Player:
    def __init__(self, name: str, balance: int, id: int):
        self.name: str = name
        self.balance: int = balance
        self.position: int = 0
        self.id: int = id
        self.prison_status: PrisonStatus = PrisonStatus()
        self.inventory: list[Card] = []

    def get_current_tile(self, board: Board) -> Tile:
        return board.get_tile_at(self.position)

    def is_in_prison(self) -> tuple[bool, int]:
        return self.prison_status.is_in_prison()
    
    def put_in_prison(self):
        self.position = PRISON_TILE
        self.prison_status.imprisonment()

    def get_score(self, board: Board) -> int:
        return self.balance + sum(
            [
                owned_tile.get_current_value()
                for owned_tile in board.get_tiles_of(self.id)
            ]
        )


class PrisonStatus:
    def __init__(self):
        self.in_prison: bool = False
        self.turns_left: int = 0

    def is_in_prison(self) -> tuple[bool, int]:
        return self.in_prison, self.turns_left

    def imprisonment(self):
        self.in_prison = True
        self.turns_left = 3

    def release(self):
        self.in_prison = False
        self.turns_left = 0

    @staticmethod
    def release_options(player: Player) -> list[tuple[str, Callable[[], bool]]]:
        options: list[tuple[str, Callable[[], bool]]] = []
        prison_status = player.prison_status

        if Card.GET_OUT_OF_JAIL_FREE in player.inventory and prison_status.turns_left > 0:
            def use_get_out_of_jail_free() -> bool:
                player.inventory.remove(Card.GET_OUT_OF_JAIL_FREE)
                player.prison_status.release()
                return True

            options.append(
                (
                    "Get Out of Jail Free card",
                    use_get_out_of_jail_free,
                )
            )
        
        if player.balance >= 50:
            def pay_50() -> bool:
                player.balance -= 50
                player.prison_status.release()
                return True

            options.append(("Pay 50", pay_50))

        if prison_status.turns_left > 0:
            def roll_dices() -> bool:
                if Die.all_equal_values(Die().throw()):
                    player.prison_status.release()
                    return True
                return False

            options.append(("Roll dice", roll_dices))

        return [(f"{i + 1} - {option[0]}", option[1]) for i, option in enumerate(options)]
