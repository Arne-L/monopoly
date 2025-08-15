from core.board import Board
from entities.player import Player
from entities.die import Die
from settings import DEFAULT_NB_OF_PLAYERS, DEFAULT_BALANCE

class Monopoly:
    def __init__(self, ):
        self.players: list[Player] = []
        self.turn = 0
        self.board = None

    def start_game(self):
        print("Starting the game ...")
        self.board = Board()
        nb_players = int(input("The number of players (default 2): ") or DEFAULT_NB_OF_PLAYERS)
        for i in range(nb_players):
            player_name = input(f"Enter name for player {i + 1}: ")
            self.players.append(Player(player_name, DEFAULT_BALANCE))
        self.die = Die()
        print(f"Game starting with {nb_players} players ...")
        self._game_loop()

    def _game_loop(self):
        assert self.board is not None, "Board has not yet been initialized"

        while True:
            current_player = self.get_current_player()
            current_tile = current_player.get_current_tile(self.board)
            print(
                f"""
                |++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
                | Player: {current_player.name}
                | Balance: {current_player.balance}
                | Current tile: {current_tile.name}
                |++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
                """
            )
            action = input("Press any key to continue or type 'stop' to forfeit\n")

            if action == "stop":
                # TODO: Remove the player from the game
                break
            else:
                # Throw the dices
                dice_total = self.die.throw_multiple(2)
                # Next tile
                new_tile = self.board.get_tile_at((current_player.position + dice_total) % len(self.board))
                print(f"The total of the dices is {dice_total}, moving towards {new_tile.name}")
                # TODO: Check for any events (passing over go, option to buy, check against balance etc)
            
            self.turn += 1
        # TODO: who is the winner & their score
        print("Game has ended!")

    def get_current_player(self) -> Player:
        return self.players[self.turn % len(self.players)]
