from core.board import Board
from entities.player import Player, PrisonStatus
from entities.die import Die
from settings import DEFAULT_NB_OF_PLAYERS, DEFAULT_BALANCE, DEFAULT_PASSING_GO_REWARD
from enum import Enum, auto

class State(Enum):
    START_GAME = auto()
    START_TURN = auto()
    """
    If in prison: 
    * Try to roll doubles (up to 3 turns) - move to roll if double, otherwise end turn
    * Use a Get Out of Jail Free card - move to roll
    * Pay $50 to leave immediately - move to roll
    else roll dice
    """
    ROLL_DICE = auto()
    """
    If double and three consecutive -> move to prison - end turn
    If double -> roll dice
    Else just move
    """
    MOVE = auto()
    """
    If passing Go: collect $200
    If unowned property:
    * Buy it - move to pay_or_buy
    * Don't buy it - action to everybody
    If owned property:
    * Pay rent - move to pay_or_buy
    * If player has a Get Out of Jail Free card, they can use it here - move to pay_or_buy
    If chance or community chest:
    * Draw a card - move to pull_card
    If tax:
    * Pay tax
    If Go to Jail:
    * Move to prison - end turn
    If Free Parking:
    * Do nothing
    """
    PAY_OR_BUY = auto()
    """
    If player has enough money:
    * Pay rent - move to end turn
    * Buy property - move to end turn
    If player does not have enough money:
    * Mortgage properties - move to mortgage
    """
    BUILDING = auto()
    """
    If player has all properties of a color:
    * Build houses/hotel - move to action
    * Sell houses/hotel - move to action
    """
    PULL_CARD = auto()
    """
    If player draws a Chance/Community Chest card:
    * Follow the instructions on the card
    """
    ACTION = auto()
    """
    Trade properties with other players + "Get Out of Jail Free" cards
    Buy/sell buildings
    (Un)Mortgage properties
    """
    PRISON = auto()
    END_TURN = auto()
    """
    If doubles, go back to ROLL_DICE
    End the turn and pass to the next player
    """
    END_GAME = auto()
    STOP = auto()

class Monopoly:
    def __init__(
        self,
    ):
        self.players: list[Player] = []
        self.turn: int = 0

    def start_game(self):
        state = State.START_GAME

        while state != State.STOP:
            state = self.handle_state(state)

    def handle_state(self, state: State) -> State:
        match state:
            case State.START_GAME:
                print("Starting the game ...")
                self.board = Board()
                nb_players = int(
                    input("The number of players (default 2): ")
                    or DEFAULT_NB_OF_PLAYERS
                )
                for i in range(nb_players):
                    player_name = input(f"Enter name for player {i + 1}: ")
                    self.players.append(Player(player_name, DEFAULT_BALANCE, i))
                self.die = Die()
                print(f"Game starting with {nb_players} players ...")
                return State.START_TURN
            case State.START_TURN:
                current_player = self.get_current_player()
                current_tile = current_player.get_current_tile(self.board)

                in_prison, prison_turns_left = current_player.is_in_prison()
                print(
                    f"""
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
| Player: {current_player.name}
| Balance: {current_player.balance}
| Current tile: {current_tile.name}
| Prison turns left: {prison_turns_left}
|++++++++++++++++++++++++++++++++++++++++++++++++++++++++++|
"""
                )

                if in_prison:
                    options = PrisonStatus.release_options(current_player)
                    prison_option = int(input(f"Choose an option to get out of jail: \n{"\n".join(map(lambda x: x[0], options))}\nOption (number): "))
                    options[prison_option - 1][1]()

                action = input("Press any key to continue or type 'stop' to forfeit\n")

                if action == "stop":
                    # TODO: Remove the player from the game instead
                    return State.END_GAME
                else:
                    return State.ROLL_DICE
            case State.ROLL_DICE:
                current_player = self.get_current_player()
                # Throw the dices
                dice_total = self.die.throw_multiple(2)
                # Positions
                old_position = current_player.position
                new_position = old_position + dice_total
                # Check passes by start / go
                nb_of_go_passes = new_position // len(self.board)

                # Next tile
                new_tile = self.board.get_tile_at(
                    (current_player.position + dice_total) % len(self.board)
                )

                # Set new position & balance
                current_player.position = new_position % len(self.board)
                current_player.balance += nb_of_go_passes * DEFAULT_PASSING_GO_REWARD

                print(
                    f"The total of the dices is {dice_total}, moving towards {new_tile.name}"
                )
                return State.END_TURN # TODO: Update with remaining steps
            case State.MOVE:
                return State.END_TURN # TODO: Implement move logic
            case State.END_TURN:
                self.turn += 1
                return State.START_TURN
            case State.END_GAME:
                print("Game has ended!")
                scoreboard = self.calc_score()
                print("The following scores where achieved:")
                for name, score in scoreboard.items():
                    print(f"{name}: {score}")
                (name, _) = max(scoreboard.items(), key=lambda pair: pair[1])
                print(f"{name} has won the game!")
                return State.STOP
            case _:
                raise ValueError(f"The provided game state {state} is has not been recognized as an existing state.")

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
                new_tile = self.board.get_tile_at(
                    (current_player.position + dice_total) % len(self.board)
                )
                print(
                    f"The total of the dices is {dice_total}, moving towards {new_tile.name}"
                )
                # TODO: Check for any events (passing over go, option to buy, check against balance etc)

            self.turn += 1
        # TODO: who is the winner & their score
        print("Game has ended!")
        scoreboard = self.calc_score()
        print("The following scores where achieved:")
        for name, score in scoreboard.items():
            print(f"{name}: {score}")
        (name, _) = max(scoreboard.items(), key=lambda pair: pair[1])
        print(f"{name} has won the game!")

    def get_current_player(self) -> Player:
        return self.players[self.turn % len(self.players)]

    def calc_score(self) -> dict[str, int]:
        assert self.board is not None, "Board has not yet been initialized"
        return {p.name: p.get_score(self.board) for p in self.players}
