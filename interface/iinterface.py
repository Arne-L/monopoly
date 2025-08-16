from abc import ABC, abstractmethod


class IInterface(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def display_board(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def initialize_game(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_number_of_players(self, default: int = 2) -> int:
        raise NotImplementedError

    @abstractmethod
    def get_player_name(self, sequence: int) -> str:
        raise NotImplementedError

    @abstractmethod
    def start_game(self, nb_of_players: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def start_turn(
        self,
        player_name: str,
        player_balance: int,
        curr_tile: str,
        in_prison: bool,
        prison_turns_left: int,
    ) -> None:
        raise NotImplementedError
