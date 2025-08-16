from enum import Enum, auto

class State(Enum):
    START_GAME = auto()
    START_TURN = auto()
    """
    If in prison: 
    * Try to roll doubles (up to 3 turns) - move to roll if double, otherwise end turn
    * Use a Get Out of Jail Free card - move to roll
    * Pay $50 to leave immediately - move to roll
    else
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
