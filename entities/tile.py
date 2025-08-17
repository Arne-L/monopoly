from abc import ABC, abstractmethod
from entities.player import Player
from core.board import Board


class Tile(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def handle_visit_of(self, player: Player, board: Board, dice_roll: int) -> None:
        raise NotImplementedError("This method should be overridden in subclasses")


class BuyableTile(Tile, ABC):
    def __init__(
        self,
        name: str,
        land_value: int,
        mortgage_value: int,
        owner: Player | None = None,
    ):
        super().__init__(name)
        self.owner = owner
        self.is_mortgaged = False
        self.land_value = land_value
        self.mortgage_value = mortgage_value

    def get_current_value(self):
        if self.is_mortgaged:
            return self.mortgage_value
        else:
            return self.land_value

    def handle_visit_of(self, player: Player, board: Board, dice_roll: int) -> None:
        if self.owner is None:
            # Get user choice
            buy_or_auction = "Buy"
            if buy_or_auction == "Buy":
                player.balance -= self.land_value
                # self.owner = player
            elif buy_or_auction == "Auction":
                # TODO: Everybody can bid on the property
                pass
            else:
                # TODO: Warning that the provided value is not the right one
                pass
        elif self.owner != player:
            rent = self.get_rent(board, dice_roll)
            transfer_success = player.transfer_to(rent, self.owner)
            if not transfer_success:
                # TODO: Handle player going bankrupt
                pass
        else:
            # TODO: Player is visiting own property, inform user
            pass

    @abstractmethod
    def get_rent(self, board: Board, dice_roll: int) -> int:
        raise NotImplementedError("Subclasses must implement this method")


class Street(BuyableTile):
    def __init__(
        self,
        name: str,
        color: str,
        land_value: int,
        base_rent: int,
        single_home_rent: int,
        double_home_rent: int,
        triple_home_rent: int,
        quadruple_home_rent: int,
        hotel_rent: int,
        home_cost: int,
        hotel_cost: int,
        mortgage_value: int,
    ):
        super().__init__(name, land_value=land_value, mortgage_value=mortgage_value)
        self.color = color
        self.base_rent = base_rent
        self.single_home_rent = single_home_rent
        self.double_home_rent = double_home_rent
        self.triple_home_rent = triple_home_rent
        self.quadruple_home_rent = quadruple_home_rent
        self.hotel_rent = hotel_rent
        self.home_cost = home_cost
        self.hotel_cost = hotel_cost
        self.nb_of_homes = 0
        self.nb_of_hotels = 0

    def get_current_value(self):
        if self.is_mortgaged:
            return self.mortgage_value
        else:
            return (
                self.land_value
                + self.home_cost * self.nb_of_homes
                + self.hotel_cost * self.nb_of_hotels
            )

    def get_rent(self, board: Board, dice_roll: int) -> int:
        if self.nb_of_hotels == 1:
            return self.hotel_rent
        elif 0 <= self.nb_of_homes <= 4:
            return [
                self.base_rent,
                self.single_home_rent,
                self.double_home_rent,
                self.triple_home_rent,
                self.quadruple_home_rent,
            ][self.nb_of_homes]
        else:
            raise ValueError("Invalid number of homes or hotels")


class Utility(BuyableTile):
    def __init__(self, name: str, land_value: int, mortgage_value: int):
        super().__init__(name, land_value=land_value, mortgage_value=mortgage_value)

    def get_rent(self, board: Board, dice_roll: int) -> int:
        utilities_owned = sum(
            1
            for tile in board.tiles
            if isinstance(tile, Utility) and tile.owner == self.owner
        )
        if utilities_owned == 1:
            return dice_roll * 4
        elif utilities_owned == 2:
            return dice_roll * 10
        else:
            raise ValueError("Invalid number of utilities owned")


class Railroad(BuyableTile):
    def __init__(
        self,
        name: str,
        land_value: int,
        mortgage_value: int,
        rent_one_station: int,
        rent_two_stations: int,
        rent_three_stations: int,
        rent_four_stations: int,
    ):
        super().__init__(name, land_value=land_value, mortgage_value=mortgage_value)
        self.rent_one_station = rent_one_station
        self.rent_two_stations = rent_two_stations
        self.rent_three_stations = rent_three_stations
        self.rent_four_stations = rent_four_stations

    def get_rent(self, board: Board, dice_roll: int) -> int:
        nb_of_stations = sum(
            1
            for tile in board.tiles
            if isinstance(tile, Railroad) and tile.owner == self.owner
        )
        if nb_of_stations == 1:
            return self.rent_one_station
        elif nb_of_stations == 2:
            return self.rent_two_stations
        elif nb_of_stations == 3:
            return self.rent_three_stations
        elif nb_of_stations == 4:
            return self.rent_four_stations
        else:
            raise ValueError("Invalid number of railroads owned")


class CardTile(Tile):
    def __init__(self, name: str, card_type: str):
        super().__init__(name)
        self.card_type = card_type

    def handle_visit_of(self, player: Player, board: Board, dice_roll: int) -> None:
        # TODO: Implement card handling logic
        raise NotImplementedError("Still to implement")


class Go(Tile):
    def __init__(self, name: str):
        super().__init__(name)

    def handle_visit_of(self, player: Player, board: Board, dice_roll: int) -> None:
        # TODO: Implement Go tile logic
        raise NotImplementedError("Still to implement")


class Jail(Tile):
    def __init__(self, name: str):
        super().__init__(name)

    def handle_visit_of(self, player: Player, board: Board, dice_roll: int) -> None:
        # TODO: Implement Jail tile logic
        raise NotImplementedError("Still to implement")


class FreeParking(Tile):
    def __init__(self, name: str):
        super().__init__(name)

    def handle_visit_of(self, player: Player, board: Board, dice_roll: int) -> None:
        # TODO: Implement Free Parking tile logic
        raise NotImplementedError("Still to implement")


class GoToJail(Tile):
    def __init__(self, name: str):
        super().__init__(name)

    def handle_visit_of(self, player: Player, board: Board, dice_roll: int) -> None:
        # TODO: Implement Go To Jail tile logic
        raise NotImplementedError("Still to implement")
