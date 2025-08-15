class Tile:
    def __init__(self, name: str):
        self.name = name


class Street(Tile):
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
        super().__init__(name)
        self.color = color
        self.land_value = land_value
        self.base_rent = base_rent
        self.single_home_rent = single_home_rent
        self.double_home_rent = double_home_rent
        self.triple_home_rent = triple_home_rent
        self.quadruple_home_rent = quadruple_home_rent
        self.hotel_rent = hotel_rent
        self.home_cost = home_cost
        self.hotel_cost = hotel_cost
        self.mortgage_value = mortgage_value


class Utility(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Railroad(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Card(Tile):
    def __init__(self, name: str, card_type: str):
        super().__init__(name)
        self.card_type = card_type


class Go(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class Jail(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class FreeParking(Tile):
    def __init__(self, name: str):
        super().__init__(name)


class GoToJail(Tile):
    def __init__(self, name: str):
        super().__init__(name)
