from interface.iinterface import IInterface


class ConsoleInterface(IInterface):
    def __init__(self):
        pass

    def display_board(self):
        pass

    def initialize_game(self):
        print("Starting the game...")

    def get_number_of_players(self, default: int = 2) -> int:
        return int(input("Enter the number of players: ") or default)

    def get_player_name(self, sequence: int) -> str:
        return input(f"Enter name for player {sequence + 1}: ")

    def start_game(self, nb_of_players: int):
        print(f"Game starting with {nb_of_players} players ...")

    def start_turn(
        self,
        player_name: str,
        player_balance: int,
        curr_tile: str,
        in_prison: bool,
        prison_turns_left: int,
    ):
        string_builder = (
            "|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|\n"
            + f"| Player: {player_name}\n"
            + f"| Balance: {player_balance}\n"
            + f"| Current tile: {curr_tile}\n"
            + (f"| Prison turns left: {prison_turns_left}\n" if in_prison else "")
            + "|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|\n"
        )

        print(string_builder)
